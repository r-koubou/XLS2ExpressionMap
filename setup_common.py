# coding: utf-8

AUTHOR = 'R-Koubou'
VERSION = '0.5.2'

options = {
    "include_files":[
        ( "README.html", "README.html" ),
        ( "LICENSE", "LICENSE" ),
        ( "NOTICE", "NOTICE" ),
        ( "Template.xlsx", "Template.xlsx" ),
    ],
    "packages": [ "os", "sys", "html", "xml", "openpyxl" ],
    "excludes": [ "tkinter" ]
}
