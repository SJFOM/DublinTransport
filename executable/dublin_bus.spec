# -*- mode: python -*-

block_cipher = None


a = Analysis(['dublin_bus.py'],
             pathex=['C:\\Users\\SOMAHONY\\Desktop\\DublinTransport\\executable'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='dublin_bus',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False , icon='dublin_bus_icon.ico')
