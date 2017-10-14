# coding: utf-8

block_cipher = None

a = Analysis(['../convert_main.py'],
             pathex=['./'],
             binaries=[],
             datas=[
                 ('../LICENSE', './'),
                 ('../NOTICE', './'),
                 ('../Template.xlsx', './Template/'),
             ],
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
          exclude_binaries=True,
          name='XLS2ExpressionMap',
          debug=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='XLS2ExpressionMap-CLI')
