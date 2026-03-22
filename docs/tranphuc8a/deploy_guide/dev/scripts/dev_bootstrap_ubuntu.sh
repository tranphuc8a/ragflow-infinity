#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

log() {
  printf '[bootstrap] %s\n' "$*"
}

need_cmd() {
  if ! command -v "$1" >/dev/null 2>&1; then
    printf 'Missing command: %s\n' "$1" >&2
    return 1
  fi
}

add_pipx_bin_to_path() {
  local pipx_bin_dir="${PIPX_BIN_DIR:-$HOME/.local/bin}"
  if [[ -d "$pipx_bin_dir" ]]; then
    export PATH="$pipx_bin_dir:$PATH"
  fi
}

resolve_bin() {
  local tool="$1"
  local pipx_bin_dir="${PIPX_BIN_DIR:-$HOME/.local/bin}"

  if command -v "$tool" >/dev/null 2>&1; then
    command -v "$tool"
    return 0
  fi

  if [[ -x "$pipx_bin_dir/$tool" ]]; then
    printf '%s\n' "$pipx_bin_dir/$tool"
    return 0
  fi

  return 1
}

log "Project root: $ROOT_DIR"

need_cmd git
need_cmd curl
need_cmd python3
need_cmd pipx

add_pipx_bin_to_path

if ! command -v uv >/dev/null 2>&1; then
  log "Installing uv via pipx"
  pipx install uv
  add_pipx_bin_to_path
fi

if ! command -v pre-commit >/dev/null 2>&1; then
  log "Installing pre-commit via pipx"
  pipx install pre-commit
  add_pipx_bin_to_path
fi

if ! UV_BIN="$(resolve_bin uv)"; then
  cat <<'EOF'
Cannot find uv after pipx installation.
Try:
  pipx ensurepath
  export PATH="$HOME/.local/bin:$PATH"
Then rerun: ./dev_bootstrap_ubuntu.sh
EOF
  exit 1
fi

if ! PRE_COMMIT_BIN="$(resolve_bin pre-commit)"; then
  cat <<'EOF'
Cannot find pre-commit after pipx installation.
Try:
  pipx ensurepath
  export PATH="$HOME/.local/bin:$PATH"
Then rerun: ./dev_bootstrap_ubuntu.sh
EOF
  exit 1
fi

# Force a stable package index to avoid broken local mirror configuration.
# You can override this when needed, for example:
#   PYPI_INDEX_URL=https://pypi.tuna.tsinghua.edu.cn/simple ./dev_bootstrap_ubuntu.sh
PYPI_INDEX_URL="${PYPI_INDEX_URL:-https://pypi.org/simple}"
export PYPI_INDEX_URL
export PIP_INDEX_URL="$PYPI_INDEX_URL"
export UV_INDEX_URL="$PYPI_INDEX_URL"
export UV_DEFAULT_INDEX="$PYPI_INDEX_URL"
export PIP_CONFIG_FILE=/dev/null
unset PIP_EXTRA_INDEX_URL UV_EXTRA_INDEX_URL || true
log "Using Python package index: $PYPI_INDEX_URL"

uv_sync_with_fallback() {
  local -a indexes=()
  local help_text
  help_text="$($UV_BIN sync --help 2>/dev/null || true)"

  # Limit resolver to current platform unless user provided a custom constraint.
  if [[ -z "${UV_ENVIRONMENTS:-}" ]]; then
    local platform
    local machine
    platform="$(uname -s | tr '[:upper:]' '[:lower:]')"
    machine="$(uname -m)"
    if [[ "$machine" == "arm64" ]]; then
      machine="aarch64"
    fi

    export UV_ENVIRONMENTS="sys_platform == '$platform' and platform_machine == '$machine'"
    log "Using uv environments filter: $UV_ENVIRONMENTS"
  else
    log "Using user-defined uv environments filter: $UV_ENVIRONMENTS"
  fi

  local -a extra_args=()
  if grep -q -- "--no-config" <<<"$help_text"; then
    extra_args+=("--no-config")
  fi
  if grep -q -- "--index-strategy" <<<"$help_text"; then
    extra_args+=("--index-strategy" "first-index")
  fi

  local has_default_index=0
  if grep -q -- "--default-index" <<<"$help_text"; then
    has_default_index=1
  fi

  if [[ -n "${PYPI_INDEX_URL:-}" ]]; then
    indexes+=("$PYPI_INDEX_URL")
  else
    indexes+=(
      "https://pypi.org/simple"
      "https://mirrors.aliyun.com/pypi/simple"
      "https://pypi.tuna.tsinghua.edu.cn/simple"
    )
  fi

  local idx
  for idx in "${indexes[@]}"; do
    log "Trying uv sync with index: $idx"
    if [[ $has_default_index -eq 1 ]]; then
      if "$UV_BIN" sync --python 3.12 --all-extras --default-index "$idx" "${extra_args[@]}"; then
        return 0
      fi
    else
      if UV_INDEX_URL="$idx" UV_DEFAULT_INDEX="$idx" "$UV_BIN" sync --python 3.12 --all-extras "${extra_args[@]}"; then
        return 0
      fi
    fi
    log "uv sync failed with index: $idx"
  done

  return 1
}

if ! command -v node >/dev/null 2>&1 || ! command -v npm >/dev/null 2>&1; then
  cat <<'EOF'
NodeJS/NPM is not installed.
Recommended quick install (Ubuntu):
  curl -fsSL https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash
  source "$HOME/.nvm/nvm.sh"
  nvm install 20
  nvm use 20
Then rerun: ./scripts/dev_bootstrap_ubuntu.sh
EOF
  exit 1
fi

log "Syncing Python dependencies into .venv"
if ! uv_sync_with_fallback; then
  cat <<'EOF'
uv sync failed on all candidate indexes.
Please try one of these commands manually:
  PYPI_INDEX_URL=https://pypi.org/simple ./dev_bootstrap_ubuntu.sh
  PYPI_INDEX_URL=https://mirrors.aliyun.com/pypi/simple ./dev_bootstrap_ubuntu.sh
  PYPI_INDEX_URL=https://pypi.tuna.tsinghua.edu.cn/simple ./dev_bootstrap_ubuntu.sh
EOF
  exit 1
fi

log "Downloading extra dependencies"
"$UV_BIN" run download_deps.py

log "Installing pre-commit hook"
"$PRE_COMMIT_BIN" install

log "Installing frontend dependencies"
(
  cd web
  npm install
)

chmod +x scripts/dev_up.sh scripts/dev_down.sh

cat <<'EOF'

Bootstrap completed.
Next step:
  ./scripts/dev_up.sh

Optional (Infinity doc engine):
  DOC_ENGINE=infinity ./scripts/dev_up.sh
EOF
