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

def genArticulation( sheet ):
    rowLength = sheet.nrows

    ret = Template.ARTICULATION_HEADER

    for row in range( 1, rowLength ):

        name = XLSUtil.getCellFromColmnName( sheet, row, "Name" ).value.strip()

        if( len( name ) == 0 ):
            break

        ret += Template.ARTICULATION.format(
            uuid1 = createUUID(),
            name  = name
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
        noteNo          = XLSUtil.getCellFromColmnName( sheet, row, "MIDI Note" ).value.strip()
        articulation    = XLSUtil.getCellFromColmnName( sheet, row, "Articulation" ).value.strip()
        vel             = XLSUtil.getCellFromColmnName( sheet, row, "Velocity" ).value
        color           = XLSUtil.getCellFromColmnName( sheet, row, "Color" ).value

        # float to int saferty
        vel   = float2int( vel )
        color = float2int( color )

        # Fail check
        if( len( name ) == 0 ):
            break

        if( len( noteNo ) > 0 and noteNo in Constants.NOTENUMBER ):
            noteNo = Constants.NOTENUMBER.index( noteNo ) # to integer format (0-127)
        else:
            noteNo = -1
            vel    = 0

        # Append articulation
        if( len( articulation ) > 0 ):
            tmp = ""
            tmp += Template.ARTICULATION_IN_SLOT_HEADER
            tmp += Template.ARTICULATION_IN_SLOT.format(
                uuid1 = createUUID(), name = articulation
            )
            tmp += Template.ARTICULATION_IN_SLOT_FOOTER
            articulation = tmp
        else:
            articulation = ""

        # Append MIDI message( Note On )
        midimessage = Template.EMPTY_MIDI_MESSAGE_IN_KEYSWITCH
        if( noteNo >= 0 ):
            midimessage = Template.MIDI_MESSAGE_IN_KEYSWITCH.format(
                uuid1 = createUUID(),
                note  = noteNo,
                vel   = vel
            )

        ret += Template.KEY_SWITCH.format(
            uuid1 = createUUID(),
            uuid2 = createUUID(),
            midimessage = midimessage,
            name  = name,
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
    keySwitchSheet    = book.sheet_by_index( 0 )
    articulationSheet = book.sheet_by_index( 1 )

    expressionMapName = os.path.splitext( xlsFilePath )[ 0 ]
    outputFileName    = expressionMapName + ".expressionmap"

    fp = open( outputFileName, "wb" )

    fp.write( Template.XML_HEADER.format( name = expressionMapName ).encode( "utf-8" ) )
    fp.write( genArticulation( articulationSheet ).encode( "utf-8" ) )
    fp.write( genKeySwitch( keySwitchSheet ).encode( "utf-8" ) )
    fp.write( Template.XML_FOOTER.encode( "utf-8" ) )

    fp.close()
    print( "{name}.expressionmap created.".format(
        name = expressionMapName
    ))

if __name__ == '__main__':
    main()
