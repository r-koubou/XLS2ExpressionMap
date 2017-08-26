# coding: utf-8

"""
MIDI Note information
"""
class MIDINote:
    def __init__( self, noteNo = -1, velocity = -1 ):
        self.noteNo   = noteNo
        self.velocity = velocity

    def valid( self ):
        return self.noteNo >= 0 and self.velocity >= 0

"""
MIDI CC information
"""
class MIDICc:
    def __init__( self, ccNo = -1, ccValue = -1 ):
        self.ccNo    = ccNo
        self.ccValue = ccValue

    def valid( self ):
        return self.ccNo >= 0 and self.ccValue >= 0

"""
MIDI PC information
"""
class MIDIPc:
    def __init__( self, lsb = -1, msb = -1 ):
        self.lsb = lsb
        self.msb = msb

    def valid( self ):
        return self.lsb >= 0 and self.msb >= 0 and self.lsb <= 255 and self.msb <= 255
