#!/usr/bin/env bash
set -euo pipefail

REPO_URL="https://github.com/alphap365/openaudio.git"
INSTALL_DIR="${OPENAUDIO_DIR:-$HOME/.local/share/openaudio}"

if ! command -v git >/dev/null 2>&1; then
    echo "Error: git is required." >&2
    exit 1
fi

if ! command -v uv >/dev/null 2>&1; then
    echo "Error: uv is required. Install it from https://docs.astral.sh/uv/getting-started/installation/." >&2
    exit 1
fi

if [ -e "$INSTALL_DIR" ]; then
    if [ ! -d "$INSTALL_DIR/.git" ]; then
        echo "Error: $INSTALL_DIR exists and is not a Git checkout. Set OPENAUDIO_DIR to another path." >&2
        exit 1
    fi

    REMOTE_URL="$(git -C "$INSTALL_DIR" remote get-url origin)"
    if [ "$REMOTE_URL" != "$REPO_URL" ]; then
        echo "Error: $INSTALL_DIR has a different origin remote; refusing to modify it." >&2
        exit 1
    fi

    git -C "$INSTALL_DIR" pull --ff-only
else
    mkdir -p "$(dirname "$INSTALL_DIR")"
    git clone --depth=1 "$REPO_URL" "$INSTALL_DIR"
fi

uv sync --project "$INSTALL_DIR"

if [ -n "${TERMUX_VERSION:-}" ] || [ -d "/data/data/com.termux" ]; then
    BIN_DIR="${PREFIX:-/data/data/com.termux/files/usr}/bin"
else
    BIN_DIR="$HOME/.local/bin"
fi

mkdir -p "$BIN_DIR"
WRAPPER_PATH="$BIN_DIR/openaudio"
printf '#!/usr/bin/env bash\ncd %q\nexec uv run openaudio "$@"\n' "$INSTALL_DIR" > "$WRAPPER_PATH"
chmod +x "$WRAPPER_PATH"

echo "OpenAudio installed to $INSTALL_DIR."
echo "Run 'openaudio' to start."
if [[ ":$PATH:" != *":$BIN_DIR:"* ]]; then
    echo "Add $BIN_DIR to PATH to run 'openaudio' from any directory."
fi
