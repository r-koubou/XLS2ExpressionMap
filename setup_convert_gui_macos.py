# coding: utf-8

import appinfo
from cx_Freeze import setup, Executable

APP_NAME   = "XLS2ExpressionMap"
executable = APP_NAME

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

exe = Executable(
    script          = 'convert_gui_main.py',
    base            = None,
    copyright       = appinfo.AUTHOR,
    targetName      = executable,
)

setup( name        = APP_NAME,
       version     = appinfo.VERSION,
       author      = appinfo.AUTHOR,
       description = 'Excel file(*.xlsx) to Cubase Expression Map file converter',
       url         = appinfo.URL,
       options     = {
           "build_exe": options,
           "bdist_mac": options_bdist_mac,
       },
       executables = [exe] )
