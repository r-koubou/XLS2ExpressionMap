# encoding: utf-8

# Convert from Cubase expression map data to csv format for XLS2ExpressionMap

import re
import sys
import html
import itertools

from xml.etree import ElementTree

from xls2expressionmap import constants

CSV_FORMAT = "{name}\t{color}\t{articulation}\t{articulationType}\t{group}\t{midiNoteNo}\t{velocity}\t{ccNo}\t{ccValue}"

class CsvRow:
    def __init__( self ):
        self.name  = ""
        self.group = 0
        self.color = 0
        self.articulationName = ""
        self.articulationType = ""
        self.midiNoteNo = ""
        self.velocity   = ""
        self.ccNo       = ""
        self.ccValue    = ""


ARGV        = sys.argv[1:]
csvRowList  = []

if( len(ARGV) == 0 ):
    print("""
usage:
    python ExpressionMap2Csv.py <file.expressionmap>
""")
    sys.exit(1)


xmlTree = ElementTree.parse( ARGV[ 0 ] )
xmlRoot = xmlTree.getroot()

outputFileName = xmlRoot.find( "./string").get( "value" ) + ".csv"
slot = xmlRoot.find( "member[@name='slots']" )

if slot == None:
    sys.exit( 1 )


def parseArticulationInfo( elem, csv ):
    # <member name="sv">
    # :
    # </member>
    name                = elem.find( "member[@name='name']/string[@name='s']")
    group               = elem.find( "member[@name='sv']/list/obj/int[@name='group']")
    articulationType    = elem.find( "member[@name='sv']/list/obj/int[@name='articulationtype']")
    color               = elem.find( "int[@name='color']")

    if( name == None or group == None or articulationType == None or color == None ):
        return

    csv.name              = html.unescape( name.get( "value" ) )
    csv.group             = int( group.get( "value" ) ) + 1
    csv.color             = color.get( "value" )
    csv.articulationName  = p.name
    csv.articulationType  = constants.ARTICULATION_TYPE[ int( articulationType.get("value") ) ]

def parseMidiEventInfo( elem, csv ):
# MIDI Event
# <obj class="PSoundSlot" ID="*****">
#     <obj class="PSlotThruTrigger" name="remote" ID="*****">
#         :
#     </obj>
#     <obj class="PSlotMidiAction" name="action" ID="*****">    <----- midiAction
#         <int name="version" value="600"/>
#         <member name="noteChanger">
#             :
#             :
#         </member>
#         <member name="midiMessages">  <------- midiMessages
#           <int name="ownership" value="1"/>
#           <list name="obj" type="obj">
#             <obj class="POutputEvent" ID="1715430416">
#                 <int name="status" value="144"/>  <--- midiStatus
#                 <int name="data1" value="17"/>    <--- midiData1
#                 <int name="data2" value="120"/>   <--- midiData2
#             </obj>
#           </list>
#         </member>
    midiAction = elem.find( "obj[@class='PSlotMidiAction']" )
    if midiAction == None:
        return

    midiMessages = midiAction.find( "member[@name='midiMessages']/list/obj[@class='POutputEvent']" )
    if midiMessages == None:
        return

    midiStatus = midiMessages.find( "int[@name='status']" )
    midiData1  = midiMessages.find( "int[@name='data1']" )
    midiData2  = midiMessages.find( "int[@name='data2']" )

    if midiStatus.get( "value" ) == "144":
        # Note On
        p.midiNoteNo = constants.NOTENUMBER[ int( midiData1.get( "value" ) ) ]
        p.velocity   = midiData2.get( "value" )
        pass
    else:
        # MIDI CC (status==177)
        p.ccNo    = midiData1.get( "value" )
        p.ccValue = midiData2.get( "value" )

# <member name="slots">
#     <int name="ownership" value="1"/>
#     <list name="obj" type="obj">
#         <obj class="PSoundSlot" ID="*****">  <-------- is i
#         :
#         :
#         </obj>
for i in slot.findall( "list/obj[@class='PSoundSlot']" ):
    p = CsvRow()
    parseArticulationInfo( i, p )
    parseMidiEventInfo( i, p )
    csvRowList.append( p )


# write to file
fp = open( outputFileName, mode = "w" )
for i in csvRowList:
    # name
    # color
    # articulation
    # articulationType
    # group
    # midiNoteNo
    # velocity
    # ccNo
    # ccValue
    fp.write( CSV_FORMAT.format(
        name                = i.articulationName,
        color               = i.color,
        articulation        = i.articulationName,
        articulationType    = i.articulationType,
        group               = i.group,
        midiNoteNo          = i.midiNoteNo,
        velocity            = i.velocity,
        ccNo                = i.ccNo,
        ccValue             = i.ccValue
    ) + "\n" )
fp.close()
print( "Result: Generated CSV -> " + outputFileName )
print( "Next:   Copy & Paste to XLS2ExpressionMap's spread sheet" )