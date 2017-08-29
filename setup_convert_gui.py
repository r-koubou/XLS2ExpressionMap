# coding: utf-8

import platform
from cx_Freeze import setup, Executable

AUTHOR = 'R-Koubou'

executable = "XLS2ExpressionMap"
base       = None
if platform.system().lower().startswith( 'win' ):
    executable += ".exe"
    base        = "Win32GUI"

options = {
    "include_files":[
        ( "convertgui.kv", "convertgui.kv" ),
        ( "resources/dropicon.png", "resources/dropicon.png" ),
    ],
    "packages": [ "os", "kivy" ],
    "excludes": [ "tkinter" ]
}

exe = Executable(
    script          = 'convert_gui_main.py',
    base            = base,
    copyright       = AUTHOR,
    targetName      = executable,
)

setup( name = 'XLS2ExpressionMap',
       version     = '0.5.1',
       author      = AUTHOR,
       description = 'Excel file(*.xlsx) to Cubase Expression Map file converter',
       url         = 'https://github.com/r-koubou/XLS2ExpressionMap',
       options     = { "build_exe": options },
       executables = [exe] )
