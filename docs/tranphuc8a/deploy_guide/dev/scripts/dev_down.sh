#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

WITH_DEPS=0
if [[ "${1:-}" == "--with-deps" ]]; then
  WITH_DEPS=1
fi

PID_DIR="$ROOT_DIR/.dev/pids"

log() {
  printf '[dev-down] %s\n' "$*"
}

stop_pidfile() {
  local name="$1"
  local pid_file="$2"

  if [[ ! -f "$pid_file" ]]; then
    log "$name pid file not found, skip"
    return 0
  fi

  local pid
  pid="$(cat "$pid_file")"
  if [[ -n "$pid" ]] && kill -0 "$pid" 2>/dev/null; then
    log "Stopping $name (pid $pid)"
    kill "$pid" || true
  else
    log "$name pid is stale, cleaning pid file"
  fi

  rm -f "$pid_file"
}

stop_pidfile "task executor" "$PID_DIR/task_executor.pid"
stop_pidfile "ragflow backend" "$PID_DIR/ragflow_server.pid"
stop_pidfile "frontend" "$PID_DIR/frontend.pid"

# Fallback in case pid files are stale or processes were started manually.
pkill -f "rag/svr/task_executor.py" >/dev/null 2>&1 || true
pkill -f "api/ragflow_server.py" >/dev/null 2>&1 || true
pkill -f "vite --host" >/dev/null 2>&1 || true

if [[ $WITH_DEPS -eq 1 ]]; then
  log "Stopping docker dependencies"
  docker compose -f docker/docker-compose.dev-deps.yml down
else
  log "Keeping docker dependencies running (use --with-deps to stop them)"
fi

log "Done"
