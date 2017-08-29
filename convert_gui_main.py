# coding: utf-8

import os
from os import path

LOGGING = False

if( LOGGING == False ):
    os.environ[ "KIVY_NO_FILELOG" ]    = "1"
    os.environ[ "KIVY_NO_CONSOLELOG" ] = "1"

#-------------------
# 3rd party modules
#-------------------
# http://kivy.org/
from kivy.app import App
from kivy.config import Config
from kivy.core.window import Window
from kivy import clock
from kivy import properties

from xls2expressionmap import convert


WINDOW_W = 400
WINDOW_H = 480

Window.minimum_width = WINDOW_W
Window.minimum_height = WINDOW_H
Window.size = ( WINDOW_W, WINDOW_H )

Config.set( "kivy", "log_enable", "0" )

"""
GUI Main window class
"""
class ConvertGUIApp( App ):

    """
    ctor
    """
    def __init__( self, **kvargs ):
        super( ConvertGUIApp, self ).__init__( **kvargs )
        self.title = "XLS2ExpressionMap GUI"
        self.message_label = properties.ObjectProperty( None )
        self.inputFilePath = ""

    def build( self ):
        Window.bind( on_dropfile = self.onDropFile )
        return super( ConvertGUIApp, self ).build()

    def onDropFile( self, window, filePath ):
        self.inputFilePath = filePath.decode()
        message = self.root.ids[ "message_label" ]
        message.text = ""
        clock.Clock.schedule_once( self.execConvert, 0 )

    def execConvert( self, deltaTime ):
        message   = self.root.ids[ "message_label" ]
        if( self.inputFilePath.endswith( ".xlsx" ) ):
            outputDir      = path.dirname( self.inputFilePath )
            try:
                conv = convert.XLS2ExpressionMap( xlsxFileName = self.inputFilePath, outputDir = outputDir )
                conv.convert()
                message.text   = "Done!"
            except:
                message.text = "Error!"

        return False

if __name__ == '__main__':
    ConvertGUIApp().run()
