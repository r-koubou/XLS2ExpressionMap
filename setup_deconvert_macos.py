# coding: utf-8

import appinfo
from cx_Freeze import setup, Executable

APP_NAME   = "ExpressionMap2Text"
executable = APP_NAME

options = {
    "include_files":[
        ( "LICENSE", "LICENSE" ),
        ( "NOTICE", "NOTICE" ),
    ],
    "excludes": [ "tkinter" ]
}

exe = Executable(
    script          = 'deconvert_main.py',
    base            = None,
    copyright       = appinfo.AUTHOR,
    targetName      = executable
)

setup( name        = 'ExpressionMap2Text',
       version     = '0.5.1',
       author      = appinfo.AUTHOR,
       description = 'Cubase Expression Map file to tab separated text converter',
       url         = appinfo.URL,
       options     = {
           "build_exe": options,
       },
       executables = [exe] )
