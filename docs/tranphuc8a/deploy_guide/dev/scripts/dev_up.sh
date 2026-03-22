#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

DOC_ENGINE="${DOC_ENGINE:-elasticsearch}"
API_PROXY_SCHEME="${API_PROXY_SCHEME:-python}"
STORAGE_IMPL="${STORAGE_IMPL:-MINIO}"
RAGFLOW_DEBUGPY_LISTEN="${RAGFLOW_DEBUGPY_LISTEN:-0}"

DEV_DIR="$ROOT_DIR/.dev"
LOG_DIR="$DEV_DIR/logs"
PID_DIR="$DEV_DIR/pids"
mkdir -p "$LOG_DIR" "$PID_DIR"

log() {
  printf '[dev-up] %s\n' "$*"
}

need_cmd() {
  if ! command -v "$1" >/dev/null 2>&1; then
    printf 'Missing command: %s\n' "$1" >&2
    exit 1
  fi
}

add_pipx_bin_to_path() {
  local pipx_bin_dir="${PIPX_BIN_DIR:-$HOME/.local/bin}"
  if [[ -d "$pipx_bin_dir" ]]; then
    export PATH="$pipx_bin_dir:$PATH"
  fi
}

resolve_uv_bin() {
  local pipx_bin_dir="${PIPX_BIN_DIR:-$HOME/.local/bin}"

  if command -v uv >/dev/null 2>&1; then
    command -v uv
    return 0
  fi

  if [[ -x "$pipx_bin_dir/uv" ]]; then
    printf '%s\n' "$pipx_bin_dir/uv"
    return 0
  fi

  return 1
}

wait_http() {
  local name="$1"
  local url="$2"
  local retries="${3:-60}"
  local delay="${4:-2}"

  log "Waiting for $name at $url"
  for ((i=1; i<=retries; i++)); do
    if curl -fsS "$url" >/dev/null 2>&1; then
      log "$name is ready"
      return 0
    fi
    sleep "$delay"
  done
  printf 'Timeout waiting for %s (%s)\n' "$name" "$url" >&2
  return 1
}

start_with_pidfile() {
  local name="$1"
  local pid_file="$2"
  local command="$3"
  local log_file="$4"

  if [[ -f "$pid_file" ]]; then
    local old_pid
    old_pid="$(cat "$pid_file")"
    if [[ -n "$old_pid" ]] && kill -0 "$old_pid" 2>/dev/null; then
      log "$name already running (pid $old_pid)"
      return 0
    fi
  fi

  log "Starting $name"
  nohup bash -lc "$command" >"$log_file" 2>&1 &
  local pid=$!
  echo "$pid" > "$pid_file"
  log "$name started (pid $pid), log: $log_file"
}

need_cmd docker
need_cmd curl
need_cmd npm

add_pipx_bin_to_path
if ! UV_BIN="$(resolve_uv_bin)"; then
  printf 'uv not found. Install with: pipx install uv, then rerun.\n' >&2
  exit 1
fi

if [[ ! -d "$ROOT_DIR/.venv" ]]; then
  printf '.venv not found. Run ./scripts/dev_bootstrap_ubuntu.sh first.\n' >&2
  exit 1
fi

if [[ ! -d "$ROOT_DIR/web/node_modules" ]]; then
  printf 'web/node_modules not found. Run ./scripts/dev_bootstrap_ubuntu.sh first.\n' >&2
  exit 1
fi

case "$DOC_ENGINE" in
  elasticsearch|infinity)
    ;;
  *)
    printf 'Unsupported DOC_ENGINE=%s. Use elasticsearch or infinity.\n' "$DOC_ENGINE" >&2
    exit 1
    ;;
esac

log "Starting docker dependencies (profile: $DOC_ENGINE)"
docker compose -f docker/docker-compose.dev-deps.yml --profile "$DOC_ENGINE" up -d

wait_http "MinIO" "http://127.0.0.1:9000/minio/health/live"
wait_http "RAGFlow ping" "http://127.0.0.1:9380/v1/system/ping" 2 1 || true

if [[ "$DOC_ENGINE" == "elasticsearch" ]]; then
  wait_http "Elasticsearch" "http://127.0.0.1:1200"
else
  wait_http "Infinity" "http://127.0.0.1:23820/admin/node/current"
fi

BACKEND_ENV="cd '$ROOT_DIR'; export PYTHONPATH='$ROOT_DIR'; export DOC_ENGINE='$DOC_ENGINE'; export STORAGE_IMPL='$STORAGE_IMPL'; export RAGFLOW_DEBUGPY_LISTEN='$RAGFLOW_DEBUGPY_LISTEN'"

start_with_pidfile \
  "task executor" \
  "$PID_DIR/task_executor.pid" \
  "$BACKEND_ENV; '$UV_BIN' run python rag/svr/task_executor.py 0" \
  "$LOG_DIR/task_executor.log"

start_with_pidfile \
  "ragflow backend" \
  "$PID_DIR/ragflow_server.pid" \
  "$BACKEND_ENV; '$UV_BIN' run python api/ragflow_server.py" \
  "$LOG_DIR/ragflow_server.log"

start_with_pidfile \
  "frontend" \
  "$PID_DIR/frontend.pid" \
  "cd '$ROOT_DIR/web'; export API_PROXY_SCHEME='$API_PROXY_SCHEME'; npm run dev" \
  "$LOG_DIR/frontend.log"

log "Waiting backend healthz"
wait_http "Backend healthz" "http://127.0.0.1:9380/v1/system/healthz"

cat <<EOF

RAGFlow dev stack is up.

- Frontend: http://127.0.0.1:9222
- Backend ping: http://127.0.0.1:9380/v1/system/ping
- Backend healthz: http://127.0.0.1:9380/v1/system/healthz

Logs:
- $LOG_DIR/task_executor.log
- $LOG_DIR/ragflow_server.log
- $LOG_DIR/frontend.log

Stop source services:
  ./scripts/dev_down.sh

Stop source + docker dependencies:
  ./scripts/dev_down.sh --with-deps
EOF
