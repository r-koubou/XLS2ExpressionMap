# coding: utf-8

import platform
from cx_Freeze import setup, Executable

import setup_common

executable = "XLS2ExpressionMap"
if platform.system().lower().startswith( 'win' ):
    executable += ".exe"

exe = Executable(
    script          = 'convert_main.py',
    base            = None,
    copyright       = setup_common.AUTHOR,
    targetName      = executable
)

setup( name = 'XLS2ExpressionMap',
       version     = setup_common.VERSION,
       author      = setup_common.AUTHOR,
       description = 'Excel file(*.xlsx) to Cubase Expression Map file converter',
       url         = 'https://github.com/r-koubou/XLS2ExpressionMap',
       options     = {
           "build_exe": setup_common.options
       },
       executables = [exe] )
