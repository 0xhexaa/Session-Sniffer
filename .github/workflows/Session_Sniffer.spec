# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.utils.hooks import collect_all

numpy_datas, numpy_binaries, numpy_hiddenimports = collect_all('numpy')

a = Analysis(
    ['..\\..\\src\\session_sniffer\\main.py'],
    pathex=['..\\..\\src'],
    binaries=[] + numpy_binaries,
    datas=[
        ('..\\..\\pyproject.toml', '.'),
        ('..\\..\\bin', 'bin'),
        ('..\\..\\images', 'images'),
        ('..\\..\\resources', 'resources'),
        ('..\\..\\scripts', 'scripts'),
        ('..\\..\\TTS', 'TTS'),
        ('..\\..\\src\\session_sniffer\\webserver\\static', 'session_sniffer\\webserver\\static'),
    ] + numpy_datas,
    hiddenimports=[] + numpy_hiddenimports,
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
    a.binaries,
    a.datas,
    [],
    name='Session_Sniffer',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    onefile=True,
)
