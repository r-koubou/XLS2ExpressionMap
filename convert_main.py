# encoding: utf-8

import sys

from xls2expressionmap import constants
from xls2expressionmap import convert
from xls2expressionmap.expressionmap import template
from xls2expressionmap.xlsx import xlsutil

def genArticulation( sheet ):
    rowLength = sheet.max_row

    ret = template.ARTICULATION_HEADER

    for row in range( 2, rowLength ):

        name = xlsutil.getValueFromColumnName( sheet, row, "Articulation" )

        if len( name ) == 0:
            break

        name = name.strip()

        artiType = xlsutil.getValueFromColumnName( sheet, row, "Articulation Type" )
        group    = getGroupValue( sheet, row )

        # Must be required values to generate
        if( len( name ) == 0 or len( artiType ) == 0 ):
            continue

        print( "[Articulation] {name}, Type={type}, Group={group}".format(
            name = name,
            type = artiType,
            group = group
        ))

        artiType = constants.ARTICULATION_TYPE.index( artiType ) # to integer format ( 0: Attribute 1: Direction).

        ret += template.ARTICULATION.format(
            uuid1 = createUUID(),
            type  = artiType,
            name  = html.escape( name ),
            group = group
        )

    ret += template.ARTICULATION_FOOTER
    return ret

def genKeySwitch( sheet ):
    rowLength = sheet.max_row

    ret = template.KEY_SWITCH_HEADER.format(
        uuid1 = createUUID(),
        uuid2 = createUUID()
    )

    for row in range( 2, rowLength ):
        name  = xlsutil.getValueFromColumnName( sheet, row, "Name" )
        if len( name ) == 0:
            break
        articulation    = xlsutil.getValueFromColumnName( sheet, row, "Articulation" )
        color           = xlsutil.getValueFromColumnName( sheet, row, "Color" )
        group           = getGroupValue( sheet, row )
        noteNo          = xlsutil.getValueFromColumnName( sheet, row, "MIDI Note" )
        vel             = xlsutil.getValueFromColumnName( sheet, row, "Velocity" )
        ccNo            = xlsutil.getValueFromColumnName( sheet, row, "CC No." )
        ccValue         = xlsutil.getValueFromColumnName( sheet, row, "CC Value" )

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
        if( len( noteNo ) > 0 and noteNo in constants.NOTENUMBER ):
            noteNo = constants.NOTENUMBER.index( noteNo ) # to integer format (0-127)
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
            tmp += template.ARTICULATION_IN_SLOT_HEADER
            tmp += template.ARTICULATION_IN_SLOT.format(
                uuid1 = createUUID(), name = articulation,
                group = group
            )
            tmp += template.ARTICULATION_IN_SLOT_FOOTER
            articulation = tmp
        else:
            articulation = ""

        # Append MIDI message( Note On / CC )
        if( noteNo < 0 and ccNo < 0 ):
            midimessage = template.EMPTY_MIDI_MESSAGE_IN_KEYSWITCH
        else:
            midimessage = template.MIDI_MESSAGE_IN_KEYSWITCH_HEADER
            if( noteNo >= 0 ):
                midimessage += template.MIDI_MESSAGE_IN_KEYSWITCH.format(
                    uuid1 = createUUID(),
                    midiMessage = 144,
                    data1       = noteNo,
                    data2       = vel
                )
            if( ccNo >= 0 ):
                midimessage += template.MIDI_MESSAGE_IN_KEYSWITCH.format(
                    uuid1 = createUUID(),
                    midiMessage = 176,
                    data1       = ccNo,
                    data2       = ccValue
                )
            midimessage += template.MIDI_MESSAGE_IN_KEYSWITCH_FOOTER

        ret += template.KEY_SWITCH.format(
            uuid1 = createUUID(),
            uuid2 = createUUID(),
            uuid3 = createUUID(),
            uuid4 = createUUID(),
            midimessage = midimessage,
            name  = html.escape( name ),
            color = color,
            articulations = articulation
        )

    ret += template.SLOTS_FOOTER
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
    book = openpyxl.load_workbook( filename = xlsFilePath, read_only = True )

    for sheetName in book.sheetnames:

        sheet = book[ sheetName ]

        # Ignore sheet
        if( sheetName == "DO NOT MODIFY!" ):
            continue

        expressionMapName = sheetName
        outputFileName    = expressionMapName + ".expressionmap"

        print( "Creating: {name}".format( name = outputFileName ) )
        fp = open( outputFileName, "wb" )

        fp.write( template.XML_HEADER.format( name = expressionMapName ).encode( "utf-8" ) )
        fp.write( genArticulation( sheet ).encode( "utf-8" ) )
        fp.write( genKeySwitch( sheet ).encode( "utf-8" ) )
        fp.write( template.XML_FOOTER.encode( "utf-8" ) )

        fp.close()

        print( "{name} created.".format(
            name = outputFileName
        ))
        print( "--------------------------------------------" )


if __name__ == '__main__':
    #main()
    from xls2expressionmap import convert
    p = convert.XLS2ExpressionMap( xlsxFileName = sys.argv[ 1 ] )
    p.convert()
