# Contributing

Contributions are welcome. For substantial changes, open an issue first to discuss the scope.

## Development setup

OpenAudio requires Python 3.13 or newer and FFmpeg. Install [uv](https://docs.astral.sh/uv/), then run:

```bash
uv sync --group dev
```

## Checks

Run the test suite and lint checks before opening a pull request:

```bash
uv run pytest
uv run ruff check src tests
```

Tests are organized by component under `tests/core`, `tests/ui`, and `tests/utils`; shared fixtures live in `tests/conftest.py`. Add focused tests for behavior changed by a contribution. Keep network-dependent tests out of the default suite; mock external services where practical.

## Pull requests

- Keep changes focused and explain the user-visible behavior.
- Update relevant documentation when commands or behavior change.
- Include test results and note any platform-specific limitations.
- Do not commit credentials, tokens, downloaded media, or local configuration.
