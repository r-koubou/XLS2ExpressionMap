# encoding: utf-8

import platform
from cx_Freeze import setup, Executable

AUTHOR = 'R-Koubou'

executable = "ExpressionMap2Text"
if platform.system().lower().startswith( 'win' ):
    executable += ".exe"

exe = Executable(
    script          = 'deconvert_main.py',
    base            = None,
    copyright       = AUTHOR,
    targetName      = executable
)

setup( name = 'XLS2ExpressionMap',
       version     = '0.0.1',
       author      = AUTHOR,
       description = 'Cubase Expression Map file to tab separated text converter',
       url         = 'https://github.com/r-koubou/XLS2ExpressionMap',
       executables = [exe] )
