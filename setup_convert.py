# coding: utf-8

import platform
from cx_Freeze import setup, Executable

AUTHOR = 'R-Koubou'

executable = "XLS2ExpressionMap"
if platform.system().lower().startswith( 'win' ):
    executable += ".exe"

exe = Executable(
    script          = 'convert_main.py',
    base            = None,
    copyright       = AUTHOR,
    targetName      = executable
)

setup( name = 'XLS2ExpressionMap',
       version     = '0.1.0',
       author      = AUTHOR,
       description = 'Excel file(*.xlsx) to Cubase Expression Map file converter',
       url         = 'https://github.com/r-koubou/XLS2ExpressionMap',
       executables = [exe] )
