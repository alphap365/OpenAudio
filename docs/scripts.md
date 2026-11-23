# Repository script usage

The scripts in `scripts/` are convenience wrappers around the project's `uv` configuration. Install Python 3.13 or newer, `uv`, and FFmpeg first. The scripts do not install `uv` or FFmpeg.

## From a source checkout

Run commands from any directory; the wrappers resolve the project root relative to themselves.

### Linux, macOS, and Termux

```bash
bash scripts/setup.sh
bash scripts/run.sh --help
bash scripts/run.sh --mobile
```

`setup.sh` runs `uv sync`. On Termux it also installs the `python` and `ffmpeg` packages through `pkg`. `run.sh` runs `uv run openaudio` and passes all arguments through to the CLI.

`openaudio_cli` is an alternate launcher equivalent to `run.sh`:

```bash
bash scripts/openaudio_cli --search "Artist Song"
```

### Windows PowerShell

```powershell
.\scripts\setup.bat
.\scripts\openaudio.bat --help
.\scripts\openaudio.bat --mobile
```

`setup.bat` runs `uv sync`; `openaudio.bat` runs `uv run openaudio` and forwards its arguments.

## Installer for Linux, macOS, and Termux

The installer clones the project into `~/.local/share/openaudio` by default, syncs its environment with uv, and creates an `openaudio` launcher in `~/.local/bin` (or `$PREFIX/bin` on Termux).

Run it from a checkout:

```bash
bash scripts/install.sh
```

Or install the latest version directly:

```bash
curl -fsSL https://raw.githubusercontent.com/alphap365/openaudio/main/scripts/install.sh | bash
```

Set `OPENAUDIO_DIR` to use another install directory:

```bash
OPENAUDIO_DIR="$HOME/apps/openaudio" bash scripts/install.sh
```

The installer requires `git` and `uv`. It does not delete an existing directory: it only updates a Git checkout whose `origin` matches OpenAudio, using a fast-forward-only pull. It refuses to modify a non-Git directory or a checkout with a different origin. Ensure the launcher's directory is on `PATH`.
