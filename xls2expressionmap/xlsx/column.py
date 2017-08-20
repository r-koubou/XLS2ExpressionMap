# encoding:utf8

from .. import constants
from ..midi import mididata

"""
The spread sheet columns structure
"""
class Columns:

    """
    ctor.
    """
    def __init__( self ):
        self.name               = ""
        self.color              = 0
        self.articulationName   = ""
        self.articulationType   = ""
        self.group              = 0
        self.noteList           = []
        self.ccList             = []
        self.pcList             = []

    """
    Convert to tab separated text format
    """
    def convertToText( self ):
        delimiter = "\t"
        ret = ""
        ret += self.name + delimiter
        ret += str( self.color ) + delimiter
        ret += self.articulationName + delimiter
        ret += self.articulationType + delimiter
        ret += str( self.group ) + delimiter

        for i in self.noteList:
            ret += i.noteNo   + delimiter
            ret += i.velocity + delimiter

        for i in self.ccList:
            ret += i.ccNo    + delimiter
            ret += i.ccValue + delimiter

        for i in self.pcList:
            ret += i.lsb + delimiter
            ret += i.msb + delimiter

        return ret
