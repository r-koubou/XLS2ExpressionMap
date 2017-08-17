# encoding: utf-8

#-------------------
# built in modules
#-------------------
import os
import sys
import html

#-------------------
# 3rd party modules
#-------------------
# https://pypi.python.org/pypi/openpyxl
import openpyxl

#-------------------
# My Script
#-------------------
from . import constants
from .util import util
from .expressionmap import template
from .xlsx import xlsutil

INT_MAX = sys.maxsize

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
        return self.ccNo >= 1 and self.ccValue >= 0

"""
Convert to xlsx file to Cubase *.expressionmap.
"""
class XLS2ExpressionMap:

    """
    ctor
    """
    def __init__( self, xlsxFileName, outputDir = '.' ):
        self.xlsxFileName = xlsxFileName
        self.book         = openpyxl.load_workbook( filename = xlsxFileName, read_only = True )
        self.outputDir    = outputDir


    """
    Generate articulation xml string from given sheet
    """
    def generateArticulation( self, sheet ):

        ret = template.ARTICULATION_HEADER

        for rowIndex in range( constants.START_ROW_INEDX, sheet.max_row ):

            name = xlsutil.getValueFromColumnName( sheet, rowIndex, constants.COLUMN_ARTICULATION )

            if name == None:
                break

            artiType = xlsutil.getValueFromColumnName( sheet, rowIndex, constants.COLUMN_ARTICULATION_TYPE )
            group    = xlsutil.getValueFromColumnName( sheet, rowIndex, constants.COLUMN_GROUP )

            # Must be required values to generate
            if name == None or artiType == None:
                continue

            print( "[Articulation] {name}, Type={type}, Group={group}".format(
                name = name,
                type = artiType,
                group = group
            ))

            artiType = constants.ARTICULATION_TYPE.index( artiType ) # to integer format ( 0: Attribute 1: Direction).

            ret += template.ARTICULATION.format(
                uuid1 = util.createUUID(),
                type  = artiType,
                name  = html.escape( name ),
                group = group
            )

        ret += template.ARTICULATION_FOOTER
        return ret

    """
    Generate velocity xml string from given sheet, row index, MIDINote instance.
    """
    def generateMIDINote( self, rowIndex, noteObj ):

        return template.MIDI_MESSAGE_IN_KEYSWITCH.format(
                    uuid1       = util.createUUID(),
                    midiMessage = 144,
                    data1       = noteObj.noteNo,
                    data2       = noteObj.velocity
        )

    """
    Generate MIDI CC xml string from given sheet and index(1-based. if multiple, set index>1 ), rowIndex index
    """
    def generateCC( self, rowIndex, cc ):

        return template.MIDI_MESSAGE_IN_KEYSWITCH.format(
                    uuid1       = util.createUUID(),
                    midiMessage = 176,
                    data1       = cc.ccNo,
                    data2       = cc.ccValue
        )

    """
    Generate key switch xml string from given sheet
    """
    def generateKeySwitch( self, sheet ):

        ret = template.KEY_SWITCH_HEADER.format(
            uuid1 = util.createUUID(),
            uuid2 = util.createUUID()
        )

        for rowIndex in range( constants.START_ROW_INEDX, sheet.max_row ):

            name = xlsutil.getValueFromColumnName( sheet, rowIndex, constants.COLUMN_NAME )
            if name == None:
                break

            articulation    = xlsutil.getValueFromColumnName( sheet, rowIndex, constants.COLUMN_ARTICULATION )
            color           = xlsutil.getValueFromColumnName( sheet, rowIndex, constants.COLUMN_COLOR )
            group           = xlsutil.getValueFromColumnName( sheet, rowIndex, constants.COLUMN_GROUP )

            print( "[Slot] {name}".format( name = name ) )

            # Append articulation
            if len( articulation ) > 0:
                tmp = ""
                tmp += template.ARTICULATION_IN_SLOT_HEADER
                tmp += template.ARTICULATION_IN_SLOT.format(
                    uuid1 = util.createUUID(), name = articulation,
                    group = group
                )
                tmp += template.ARTICULATION_IN_SLOT_FOOTER
                articulation = tmp
            else:
                articulation = ""

            # Append MIDI Notes
            # * Multiple MIDI Note Supported
            # * Column name format:
            #   MIDI Note1 ... MIDI Note1+n
            #   Velocity1 ... Velocity1+n
            midiNoteList = []
            midiMessageXml = ""
            for i in range( 1, INT_MAX ):
                noteNo = xlsutil.getValueFromColumnName( sheet, rowIndex, constants.COLUMN_MIDI_NOTE + str( i ) )
                vel    = xlsutil.getValueFromColumnName( sheet, rowIndex, constants.COLUMN_MIDI_VELOCITY + str( i ) )
                if noteNo == None or vel == None:
                    break

                if noteNo in constants.NOTENUMBER:
                    noteNo = constants.NOTENUMBER.index( noteNo ) # to integer format (0-127)

                obj = MIDINote( noteNo, vel )
                if obj.valid:
                    midiNoteList.append( obj )

            if len( midiNoteList ) > 0:

                midiMessageXml += template.MIDI_MESSAGE_IN_KEYSWITCH_HEADER

                for n in midiNoteList:
                    midiMessageXml += self.generateMIDINote( rowIndex, n )

                midiMessageXml += template.MIDI_MESSAGE_IN_KEYSWITCH_FOOTER

            # Append MIDI CC
            # * Multiple MIDI CC Supported
            # * Column name format:
            #   CC No1 ... CC No1+n
            #   CC Value1 ... CC Value1+n
            ccList = []
            midiMessageXml = ""

            for i in range( 1, INT_MAX ):
                ccNo    = xlsutil.getValueFromColumnName( sheet, rowIndex, constants.COLUMN_MIDI_CC + str( i ) )
                ccValue = xlsutil.getValueFromColumnName( sheet, rowIndex, constants.COLUMN_MIDI_CC_VALUE + str( i ) )
                if ccNo == None or ccValue == None:
                    break

                obj = MIDICc( ccNo, ccValue )
                if obj.valid:
                    ccList.append( obj )

            if len( ccList ) > 0:

                midiMessageXml += template.MIDI_MESSAGE_IN_KEYSWITCH_HEADER

                for cc in ccList:
                    midiMessageXml += self.generateCC( rowIndex, cc )

                midiMessageXml += template.MIDI_MESSAGE_IN_KEYSWITCH_FOOTER

            # Generate Keyswitch XML text
            ret += template.KEY_SWITCH.format(
                uuid1 = util.createUUID(),
                uuid2 = util.createUUID(),
                uuid3 = util.createUUID(),
                uuid4 = util.createUUID(),
                midimessage = midiMessageXml,
                name  = html.escape( name ),
                color = color,
                articulations = articulation
            )

        return ret

    """
    Convert to Expression map file
    """
    def convert( self ):
        for sheetName in self.book.sheetnames:

            xmlText = ''
            sheet   = self.book[ sheetName ]

            # Ignore sheet
            if sheetName == constants.LIST_DEFINITION_SHEETNAME:
                continue

            expressionMapName = sheetName
            outputFileName    = expressionMapName + ".expressionmap"
            xmlText  = template.XML_HEADER.format( name = expressionMapName )
            xmlText += self.generateArticulation( sheet )
            xmlText += self.generateKeySwitch( sheet )

            xmlText = xmlText.encode( 'utf8' )

            fp = open( outputFileName, "wb" )
            fp.write( xmlText )
            fp.close()

