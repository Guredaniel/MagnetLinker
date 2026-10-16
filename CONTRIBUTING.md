# Contributing

Thanks for helping improve MagnetLinker.

## Before opening an issue

- Search existing issues to avoid duplicates.
- For bugs, include your operating system, Python version (when running from source), steps to reproduce, and any relevant error message.
- Do not include passwords, private URLs, IP addresses, or files from MagnetLinker's application data directory.

## Development setup

Use Python 3.12 or newer and create a virtual environment in the repository root.

### Windows

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

### macOS

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-macos.txt
```

## Tests

On macOS, install the test dependencies and run the suite from the repository root:

```bash
python -m pip install -e ".[test,macos]"
python -m pytest -q
```

Some tests cover macOS-specific UI behavior. Please mention your operating system and the test command you ran in your pull request.

## Project layout

- Application code and packaged icons: `src/magnetlinker/`
- Automated tests: `tests/`
- Project documentation: `docs/`
- Build scripts: `scripts/`

## Pull requests

- Keep changes focused and explain the user-visible behavior they change.
- Update documentation when setup or behavior changes.
- Run the relevant tests and report the result. If a test cannot run on your platform, say so.
- Do not commit virtual environments, build output, credentials, or local application settings.
