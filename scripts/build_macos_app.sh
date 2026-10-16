#!/usr/bin/env bash
set -euo pipefail

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

# Activate virtualenv if present
if [ -f "$PROJECT_ROOT/.venv/bin/activate" ]; then
  # shellcheck disable=SC1091
  source "$PROJECT_ROOT/.venv/bin/activate"
fi

# Use venv Python only; fail loudly if missing
if [ -x "$PROJECT_ROOT/.venv/bin/python" ]; then
  PYTHON="$PROJECT_ROOT/.venv/bin/python"
else
  echo "Error: .venv/bin/python not found. Please create/activate the virtualenv." >&2
  exit 1
fi

cd "$PROJECT_ROOT"

echo "Installing macOS requirements..."
"$PYTHON" -m pip install -r requirements-macos.txt

echo "Building MagnetLinker app..."
"$PYTHON" -m PyInstaller --noconfirm --clean --distpath dist --workpath build src/magnetlinker/MagnetLinker.spec

echo "Build finished. .app should be in the 'dist' directory."