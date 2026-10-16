# MagnetLinker

MagnetLinker is a desktop companion for [qBittorrent](https://www.qbittorrent.org/). It watches your clipboard for magnet links and helps route downloads to the right movie or series directory. It also supports sending a magnet link manually and adding `.torrent` files.

| Platform | Build |
| --- | --- |
| Windows | [![Build MagnetLinker (Windows)](https://github.com/Guredaniel/MagnetLinker/actions/workflows/build-windows.yml/badge.svg)](https://github.com/Guredaniel/MagnetLinker/actions/workflows/build-windows.yml) |
| macOS | [![Build MagnetLinker (macOS)](https://github.com/Guredaniel/MagnetLinker/actions/workflows/build-macos.yml/badge.svg)](https://github.com/Guredaniel/MagnetLinker/actions/workflows/build-macos.yml) |

## Features

- Detect magnet links copied to the clipboard and prompt for a content type.
- Choose movie or series download directories, with optional alternative directories.
- Remember content-type choices for a configurable period.
- Send magnet links or `.torrent` files to qBittorrent.
- Configure clipboard monitoring, download paths, qBittorrent connection details, and saved site links.
- Use the Windows system tray or the macOS menu bar interface.

## Requirements

- Python 3.12 or newer.
- qBittorrent with its Web UI enabled and reachable from this computer.
- macOS users: the macOS-specific dependencies include PyObjC and require macOS.

## Get the app

Published versions are listed on the [Releases page](https://github.com/Guredaniel/MagnetLinker/releases). Some releases include downloadable app builds; future tag-triggered releases may contain release notes only.

If a release does not include a download, you can get a temporary build from GitHub Actions:

1. Open the [Actions](https://github.com/Guredaniel/MagnetLinker/actions) page and select a successful Windows or macOS build.
2. Download the matching artifact (`MagnetLinker-Windows` or `MagnetLinker-macOS`) from the run's **Artifacts** section. You must be signed in to GitHub to download workflow artifacts.
3. On macOS, open `MagnetLinker.dmg` and move the app to your preferred location.

Actions artifacts are temporary workflow outputs, not signed installers or permanent releases. They may expire according to GitHub's artifact-retention settings.

### Publish a release

Push a version tag beginning with `v` to create a GitHub Release with automatically generated notes. This workflow does not build or attach downloads:

```bash
git tag v1.3
git push origin v1.3
```

Use a new tag for each release. You can tag the current commit even when there are no new code changes; GitHub will still publish a release for that tag.

## Run from source

### Windows

In PowerShell, from the repository root:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m magnetlinker
```

### macOS

In Terminal, from the repository root:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-macos.txt
python -m magnetlinker
```

The macOS app uses a native menu bar interface when its macOS dependencies are installed. Otherwise, the entry point falls back to the cross-platform interface.

## Configure qBittorrent

1. In qBittorrent, enable the Web UI and make sure it is reachable from the computer running MagnetLinker.
2. Launch MagnetLinker and open **Settings**.
3. Enter the qBittorrent Web UI URL, movie and series save paths, and any optional alternative paths.
4. Enter your qBittorrent credentials, then use **Test Connection** to verify the connection.
5. Choose whether clipboard monitoring is enabled and adjust the behavior to suit your workflow.

Use the URL and paths appropriate to your qBittorrent setup; the defaults may not match your computer or network. If connecting to a remote qBittorrent server, use a trusted network and secure the Web UI appropriately.

## Build

The GitHub Actions workflows build on their respective operating systems and upload artifacts:

- [Windows workflow](.github/workflows/build-windows.yml)
- [macOS workflow](.github/workflows/build-macos.yml)

To build locally on Windows, install the platform requirements above and run:

```powershell
python -m PyInstaller --noconfirm --clean --onefile --windowed `
  --paths src --name MagnetLinker --icon src/magnetlinker/assets/icon.png `
  --collect-all customtkinter `
  --add-data "src/magnetlinker/assets/icon.png;magnetlinker/assets" `
  src/magnetlinker/MagnetApp.py
```

On macOS, run the build script from any directory:

```bash
bash scripts/build_macos_app.sh
```

## Tests

On macOS, install the test dependencies and run the suite from the repository root:

```bash
python -m pip install -e ".[test,macos]"
python -m pytest -q
```

Some tests exercise macOS-specific UI behavior. The GitHub Actions workflows currently validate application packaging; they do not run the test suite.

## Project layout

```text
src/magnetlinker/   Application package and packaged artwork
tests/              Automated tests and test runner
docs/               Project and test documentation
scripts/            Local build helpers
.github/workflows/  Build and release automation
```

## Settings and credentials

MagnetLinker stores settings and qBittorrent credentials in its per-user application data directory:

- Windows: `%USERPROFILE%\AppData\Local\MagnetLinker`
- macOS: `~/Library/Application Support/MagnetLinker`
- Linux/other Unix: `~/.local/share/MagnetLinker`

Credentials are encrypted locally using Fernet, with the encryption key stored alongside the credential file. This protects the saved values from casual inspection, but does not protect them from someone with access to your user account or application data directory. Do not share this directory or include it in bug reports.

## Contributing

Bug reports, feature ideas, and pull requests are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request, and use the available issue templates when reporting a bug or proposing a feature.

## License

No license is currently included in this repository. Unless a license is added, the code is not explicitly granted for reuse or redistribution.
