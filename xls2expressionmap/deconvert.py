# coding: utf-8

# Convert from Cubase expression map data to csv format for XLS2ExpressionMap

import os
import html

from xml.etree import ElementTree

from . import constants
from .midi import mididata
from .xlsx import column

"""
Expression map file to Tab separated plain text (Copy and paste to spread sheet)
"""
class ExpressionMap2Text:

    """
    ctor.
    """
    def __init__( self, sourceFileName ):
        self.sourceFileName = sourceFileName
        self.xmlTree    = ElementTree.parse( sourceFileName )
        self.xmlRoot    = self.xmlTree.getroot()
        self.slot       = self.xmlRoot.find( "member[@name='slots']" )
        self.rows       = []

    """
    deconvert
    """
    def deconvert( self ):

        if self.slot == None:
            return

        # <member name="slots">
        #     <int name="ownership" value="1"/>
        #     <list name="obj" type="obj">
        #         <obj class="PSoundSlot" ID="*****">  <-------- is i
        #         :
        #         :
        #         </obj>
        outputText = ""
        for i in self.slot.findall( "list/obj[@class='PSoundSlot']" ):
            p = column.Columns()
            self.parseArticulationInfo( p, i )
            self.rows.append( p )
            outputText += p.convertToText() + os.linesep

        outputText = outputText.encode( "utf8" )

        fp = open( self.sourceFileName + ".txt", "wb" )
        fp.write( outputText )
        fp.close()

    def parseArticulationInfo( self, row, elem ):
        # <member name="sv">
        # :
        # </member>
        name                = elem.find( "member[@name='name']/string[@name='s']")
        group               = elem.find( "member[@name='sv']/list/obj/int[@name='group']")
        articulationType    = elem.find( "member[@name='sv']/list/obj/int[@name='articulationtype']")
        color               = elem.find( "int[@name='color']")

        if( name == None or group == None or articulationType == None or color == None ):
            return

        row.name              = html.unescape( name.get( "value" ) )
        row.color             = color.get( "value" )
        row.articulationName  = row.name
        row.articulationType  = constants.ARTICULATION_TYPE[ int( articulationType.get("value") ) ]
        row.group             = int( group.get( "value" ) )

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
        #         <member name="midiMessages">
        #           <int name="ownership" value="1"/>
        #           <list name="obj" type="obj">            <------- midiMessages
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

        midiMessages = midiAction.findall( "member[@name='midiMessages']/list/obj[@class='POutputEvent']" )
        if midiMessages == None:
            return

        for obj in midiMessages:
            midiStatus = obj.find( "int[@name='status']" )
            midiData1  = obj.find( "int[@name='data1']" )
            midiData2  = obj.find( "int[@name='data2']" )

            midiStatusValue = midiStatus.get( "value" )

            if midiStatusValue == "144":
                # Note On
                p = mididata.MIDINote()
                p.noteNo = constants.NOTENUMBER[ int( midiData1.get( "value" ) ) ]
                p.velocity   = midiData2.get( "value" )
                row.noteList.append( p )
                pass
            elif midiStatusValue == "176":
                # MIDI CC
                p = mididata.MIDICc()
                p.ccNo    = midiData1.get( "value" )
                p.ccValue = midiData2.get( "value" )
                row.ccList.append( p )
            elif midiStatusValue == "192":
                # MIDI Program Change
                p = mididata.MIDIPc()
                p.lsb = midiData1.get( "value" )
                p.msb = midiData2.get( "value" )
                row.pcList.append( p )
