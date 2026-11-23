@echo off
setlocal
pushd "%~dp0.." || exit /b 1
where uv >nul 2>nul
if errorlevel 1 (
    echo Error: uv is required. Install it from https://docs.astral.sh/uv/getting-started/installation/.
    popd
    exit /b 1
)
uv run opentunes %*
set "EXIT_CODE=%ERRORLEVEL%"
popd
exit /b %EXIT_CODE%
