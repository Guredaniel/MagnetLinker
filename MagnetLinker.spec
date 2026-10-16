# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['MagnetApp.py'],
    pathex=[],
    binaries=[],
    datas=[('icon.png', '.'), ('icon.icns', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='MagnetLinker',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['icon.icns'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='MagnetLinker',
)
app = BUNDLE(
    coll,
    name='MagnetLinker.app',
    icon='icon.icns',
    bundle_identifier='com.magnetlinker.app',
    plist={
        'CFBundleIdentifier': 'com.magnetlinker.app',
        'CFBundleURLTypes': [
            {
                'CFBundleURLName': 'magnet',
                'CFBundleURLSchemes': ['magnet'],
            }
        ],
    },
)
