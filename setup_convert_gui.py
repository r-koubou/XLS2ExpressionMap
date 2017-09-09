# coding: utf-8

import platform
from cx_Freeze import setup, Executable

APP_NAME = "XLS2ExpressionMap"
AUTHOR   = 'R-Koubou'
VERSION  = "0.5.1"

executable = APP_NAME
base       = None
if platform.system().lower().startswith( 'win' ):
    executable += ".exe"
    base        = "Win32GUI"

options = {
    "include_files":[
        ( "LICENSE", "LICENSE" ),
        ( "NOTICE", "NOTICE" ),
        ( "convertgui.kv", "convertgui.kv" ),
        ( "resources/dropicon.png", "resources/dropicon.png" ),
    ],
    "packages": [ "os", "kivy" ],
    "excludes": [ "tkinter" ]
}

options_bdist_mac = {
    "custom_info_plist": "macos/Info.plist",
    "bundle_name":       APP_NAME,
    "iconfile":          "macos/icon.icns",
}

options_bdist_dmg = {
    "volume_label": "XLS2ExpressionMap",
    "applications_shortcut": True,
}

exe = Executable(
    script          = 'convert_gui_main.py',
    base            = base,
    copyright       = AUTHOR,
    targetName      = executable,
)

setup( name        = APP_NAME,
       version     = VERSION,
       author      = AUTHOR,
       description = 'Excel file(*.xlsx) to Cubase Expression Map file converter',
       url         = 'https://github.com/r-koubou/XLS2ExpressionMap',
       options     = {
           "build_exe": options,
           "bdist_mac": options_bdist_mac,
           "bdist_dmg": options_bdist_dmg,
       },
       executables = [exe] )
