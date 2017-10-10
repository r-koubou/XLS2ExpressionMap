# coding: utf-8

from cx_Freeze import setup, Executable

AUTHOR = 'R-Koubou'

exe = Executable(
    script          = 'deconvert_main.py',
    base            = None,
    copyright       = AUTHOR,
    targetName      = executable
)

setup( name = 'XLS2ExpressionMap',
       version     = '0.5.1',
       author      = AUTHOR,
       description = 'Cubase Expression Map file to tab separated text converter',
       url         = 'https://github.com/r-koubou/XLS2ExpressionMap',
       executables = [exe] )
