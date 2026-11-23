#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"

if [ -n "${TERMUX_VERSION:-}" ] || [ -d "/data/data/com.termux" ]; then
    pkg install -y python ffmpeg
fi

if ! command -v uv >/dev/null 2>&1; then
    echo "Error: uv is required. Install it from https://docs.astral.sh/uv/getting-started/installation/." >&2
    exit 1
fi

cd "$PROJECT_DIR"
uv sync
chmod +x "$SCRIPT_DIR/run.sh" "$SCRIPT_DIR/opentunes_cli"
echo "OpenTunes is ready. Run 'bash scripts/run.sh --help' to see options."
