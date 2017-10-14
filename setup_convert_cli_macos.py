# coding: utf-8

import appinfo
from cx_Freeze import setup, Executable

APP_NAME   = "XLS2ExpressionMap"
executable = APP_NAME

options = {
    "include_files":[
        ( "LICENSE", "LICENSE" ),
        ( "NOTICE", "NOTICE" ),
    ],
    "excludes": [ "tkinter" ]
}

exe = Executable(
    script          = 'convert_main.py',
    base            = None,
    copyright       = appinfo.AUTHOR,
    targetName      = executable
)

setup( name        = APP_NAME,
       version     = appinfo.VERSION,
       author      = appinfo.AUTHOR,
       description = 'Excel file(*.xlsx) to Cubase Expression Map file converter',
       url         = appinfo.URL,
       options     = {
           "build_exe": options,
       },
       executables = [exe] )
