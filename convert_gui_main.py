# coding: utf-8

import threading
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
        self.converter = None
        self.finished  = False

    def build( self ):
        Window.bind( on_dropfile = self.onDropFile )
        return super( ConvertGUIApp, self ).build()

    def onDropFile( self, window, filePath ):
        self.inputFilePath = filePath.decode()
        message = self.root.ids[ "message_label" ]

        if( self.converter != None and self.converter.is_alive() ):
            return

        self.finished  = False
        self.converter = ConvertThread( xlsxFilePath=self.inputFilePath, callback=self.onConvertFinished )
        self.converter.start()

        message.text = "Processing..."
        clock.Clock.schedule_interval( self.onConvertProgress, 0.05 )

    def onConvertProgress( self, deltaTime ):
        message = self.root.ids[ "progress_label" ]
        if( self.finished == True ):
            message.text = ""
            return
        if( len( message.text ) > 16 ):
            message.text = ""

        message.text = message.text + "-"
        return self.finished != True

    def onConvertFinished( self ):
        self.finished   = True
        message         = self.root.ids[ "message_label" ]
        progressMessage = self.root.ids[ "progress_label" ]
        progressMessage.text = ""
        if( self.converter.result == True ):
            message.text   = "Done!"
        else:
            message.text   = "Error!"

"""
Convert processing outside UI thread
"""
class ConvertThread( threading.Thread ):

    """
    ctor.
    """
    def __init__( self, xlsxFilePath, callback=None ):
        super( ConvertThread, self ).__init__()
        self.xlsxFilePath   = xlsxFilePath
        self.result         = False
        self.callback       = callback

    def run( self ):
        if( self.xlsxFilePath.endswith( ".xlsx" ) ):
            outputDir = path.dirname( self.xlsxFilePath )
            try:
                conv = convert.XLS2ExpressionMap( xlsxFileName = self.xlsxFilePath, outputDir = outputDir )
                conv.convert()
                self.result = True
            except:
                self.result = False
            finally:
                if( self.callback != None ):
                    self.callback()


if __name__ == '__main__':
    ConvertGUIApp().run()
