# -*- mode: python -*-

block_cipher = None
import sys
import os

spec_root = os.path.abspath(SPECPATH)
print(30*'-')
print(spec_root)
print(30*'-')

a = Analysis(['main.py'],
             pathex=[],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
a.datas += []
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
if sys.platform == 'darwin':
  exe = EXE(pyz,
            a.scripts,
            a.binaries,
            a.zipfiles,
            a.datas,
            name='banana',
            debug=False,
            strip=False,
            upx=True,
            runtime_tmpdir=None,
            console=True,
            icon='assets/banana.icns')
elif sys.platform == 'win32' or sys.platform == 'win64':
  exe = EXE(pyz,
            a.scripts,
            a.binaries,
            a.zipfiles,
            a.datas,
            name='banana',
            debug=False,
            strip=False,
            upx=True,
            runtime_tmpdir=None,
            console=False,
            icon='assets/banana.ico')
elif sys.platform == 'linux':
  exe = EXE(pyz,
            a.scripts,
            a.binaries,
            a.zipfiles,
            a.datas,
            name='banana',
            debug=False,
            strip=False,
            upx=True,
            runtime_tmpdir=None,
            console=False,
            icon='assets/banana.ico')

# Build a .app if on OS X
if sys.platform == 'darwin':
   app = BUNDLE(exe,
                name='banana.app',
                info_plist={
                  'NSHighResolutionCapable': 'True'
                },
                icon='assets/banana.icns')