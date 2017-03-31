# encoding: utf-8

# MIT License
#
# Copyright (c) 2017 R-Koubou
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

#-------------------
# built in libs
#-------------------
import os
import sys
import uuid
import html

#-------------------
# 3rd party libs
#-------------------
# http://pypi.python.org/pypi/xlrd
import xlrd

#-------------------
# my scripts
#-------------------
import Constants
import Template
import XLSUtil

def createUUID():
    return uuid.uuid4().fields[ 0 ]

def createUUIDList( listSize ):
    ret = [0] * listSize
    for i in range( listSize ):
          ret[ i ] = uuid.uuid4().fields[ 0 ]

    return ret

def float2int( v, defaultValue = 0 ):
    if( isinstance( v, float ) ):
        return int( v )
    else:
        return defaultValue

def getGroupValue( sheet, row ):
    group = XLSUtil.getCellFromColmnName( sheet, row, "Group" )

    # Since v0.0.5: Colmn "Group" check (+backward compatibility)
    if( group != None and hasattr( group, "value" ) ):
        # float to int saferty
        group   = float2int( group.value ) - 1

        if( group < 0 ):
            group = 0
    else:
        group = 0

    return group

def genArticulation( sheet ):
    rowLength = sheet.nrows

    ret = Template.ARTICULATION_HEADER

    for row in range( 1, rowLength ):

        name     = XLSUtil.getCellFromColmnName( sheet, row, "Articulation" ).value.strip()
        artiType = XLSUtil.getCellFromColmnName( sheet, row, "Articulation Type" ).value.strip()
        group    = getGroupValue( sheet, row )

        # Must be required values to generate
        if( len( name ) == 0 or len( artiType ) == 0 ):
            continue

        print( "[Articulation] {name}, Type={type}, Group={group}".format(
            name = name,
            type = artiType,
            group = group
        ))

        artiType = Constants.ARTICULATION_TYPE.index( artiType ) # to integer format ( 0: Attribute 1: Direction).

        ret += Template.ARTICULATION.format(
            uuid1 = createUUID(),
            type  = artiType,
            name  = html.escape( name ),
            group = group
        )

    ret += Template.ARTICULATION_FOOTER
    return ret

def genKeySwitch( sheet ):
    rowLength = sheet.nrows

    ret = Template.KEY_SWITCH_HEADER.format(
        uuid1 = createUUID(),
        uuid2 = createUUID()
    )

    for row in range( 1, rowLength ):
        name            = XLSUtil.getCellFromColmnName( sheet, row, "Name" ).value.strip()
        articulation    = XLSUtil.getCellFromColmnName( sheet, row, "Articulation" ).value.strip()
        color           = XLSUtil.getCellFromColmnName( sheet, row, "Color" ).value
        group           = getGroupValue( sheet, row )
        noteNo          = XLSUtil.getCellFromColmnName( sheet, row, "MIDI Note" ).value.strip()
        vel             = XLSUtil.getCellFromColmnName( sheet, row, "Velocity" ).value
        ccNo            = XLSUtil.getCellFromColmnName( sheet, row, "CC No." ).value
        ccValue         = XLSUtil.getCellFromColmnName( sheet, row, "CC Value" ).value

        # float to int saferty
        vel     = float2int( vel )
        color   = float2int( color )
        ccNo    = float2int( ccNo, -1 )
        ccValue = float2int( ccValue, -1 )

        # Fail check
        if( len( name ) == 0 ):
            break

        print( "[Slot] {name}".format( name = name ) )

        # MIDI Message check( Note On )
        if( len( noteNo ) > 0 and noteNo in Constants.NOTENUMBER ):
            noteNo = Constants.NOTENUMBER.index( noteNo ) # to integer format (0-127)
        else:
            noteNo = -1
            vel    = 0

        # MIDI Message check( CC )
        if( ccNo < 0 or ccValue < 0 ):
            ccNo    = -1
            ccValue = -1

        # Append articulation
        if( len( articulation ) > 0 ):
            tmp = ""
            tmp += Template.ARTICULATION_IN_SLOT_HEADER
            tmp += Template.ARTICULATION_IN_SLOT.format(
                uuid1 = createUUID(), name = articulation,
                group = group
            )
            tmp += Template.ARTICULATION_IN_SLOT_FOOTER
            articulation = tmp
        else:
            articulation = ""

        # Append MIDI message( Note On / CC )
        if( noteNo < 0 and ccNo < 0 ):
            midimessage = Template.EMPTY_MIDI_MESSAGE_IN_KEYSWITCH
        else:
            midimessage = Template.MIDI_MESSAGE_IN_KEYSWITCH_HEADER
            if( noteNo >= 0 ):
                midimessage += Template.MIDI_MESSAGE_IN_KEYSWITCH.format(
                    uuid1 = createUUID(),
                    midiMessage = 144,
                    data1       = noteNo,
                    data2       = vel
                )
            if( ccNo >= 0 ):
                midimessage += Template.MIDI_MESSAGE_IN_KEYSWITCH.format(
                    uuid1 = createUUID(),
                    midiMessage = 176,
                    data1       = ccNo,
                    data2       = ccValue
                )
            midimessage += Template.MIDI_MESSAGE_IN_KEYSWITCH_FOOTER

        ret += Template.KEY_SWITCH.format(
            uuid1 = createUUID(),
            uuid2 = createUUID(),
            uuid3 = createUUID(),
            uuid4 = createUUID(),
            midimessage = midimessage,
            name  = html.escape( name ),
            color = color,
            articulations = articulation
        )

    ret += Template.SLOTS_FOOTER
    return ret

def usage():
    print(
"""---------------------
  XLS2ExpressionMap
  2017 (c) R-Koubou
---------------------
usage:
    python XLS2ExpressionMap.py <input file>
    <input file>: xlsx file path
        """
    )

def main():

    if( len( sys.argv ) < 2 ):
        usage()
        return

    xlsFilePath = sys.argv[ 1 ]
    book              = xlrd.open_workbook( xlsFilePath )

    for sheet in book.sheets():

        # Ignore sheet
        if( sheet.name == "DO NOT MODIFY!" ):
            continue

        expressionMapName = sheet.name
        outputFileName    = expressionMapName + ".expressionmap"

        print( "Creating: {name}".format( name = outputFileName ) )
        fp = open( outputFileName, "wb" )

        fp.write( Template.XML_HEADER.format( name = expressionMapName ).encode( "utf-8" ) )
        fp.write( genArticulation( sheet ).encode( "utf-8" ) )
        fp.write( genKeySwitch( sheet ).encode( "utf-8" ) )
        fp.write( Template.XML_FOOTER.encode( "utf-8" ) )

        fp.close()

        print( "{name} created.".format(
            name = outputFileName
        ))
        print( "--------------------------------------------" )


if __name__ == '__main__':
    main()
