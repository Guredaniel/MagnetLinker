# MagnetLinker

MagnetLinker is a desktop companion for [qBittorrent](https://www.qbittorrent.org/). It watches your clipboard for magnet links and helps route downloads to the right movie or series directory. It also supports sending a magnet link manually and adding `.torrent` files.

| Platform | Build |
| --- | --- |
| Windows | [![Build MagnetLinker (Windows)](https://github.com/Guredaniel/UpcomingEpisodes/actions/workflows/build-windows.yml/badge.svg)](https://github.com/Guredaniel/UpcomingEpisodes/actions/workflows/build-windows.yml) |
| macOS | [![Build MagnetLinker (macOS)](https://github.com/Guredaniel/UpcomingEpisodes/actions/workflows/build-macos.yml/badge.svg)](https://github.com/Guredaniel/UpcomingEpisodes/actions/workflows/build-macos.yml) |

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

There are no published release downloads yet. To download a build produced by GitHub Actions:

1. Open the [Actions](https://github.com/Guredaniel/UpcomingEpisodes/actions) page and select a successful Windows or macOS build.
2. Download the matching artifact (`MagnetLinker-Windows` or `MagnetLinker-macOS`) from the run's **Artifacts** section. You must be signed in to GitHub to download workflow artifacts.
3. On macOS, open `MagnetLinker.dmg` and move the app to your preferred location.

Artifacts are temporary workflow outputs, not signed installers or permanent releases. They may expire according to GitHub's artifact-retention settings.

## Run from source

### Windows

In PowerShell, from the repository root:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python MagnetApp.py
```

### macOS

In Terminal, from the repository root:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-macos.txt
python MagnetApp.py
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

To build locally, install the platform requirements above and run:

```bash
python -m PyInstaller --noconfirm --clean --onefile --windowed \
  --name MagnetLinker --icon icon.png --collect-all customtkinter \
  --add-data "icon.png;." MagnetApp.py
```

On Windows, PyInstaller uses `;` to separate bundled data paths:

```powershell
python -m PyInstaller --noconfirm --clean --onefile --windowed `
  --name MagnetLinker --icon icon.png --collect-all customtkinter `
  --add-data "icon.png;." MagnetApp.py
```

On macOS, use the provided spec file:

```bash
python -m PyInstaller --noconfirm --clean MagnetLinker.spec
```

## Tests

Install the platform requirements, then run the test suite from the repository root:

```bash
python -m pytest -q Tests-Mac
```

Some tests exercise macOS-specific UI behavior. The GitHub Actions workflows currently validate application packaging; they do not run the test suite.

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
