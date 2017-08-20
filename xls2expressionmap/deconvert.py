# encoding: utf-8

# Convert from Cubase expression map data to csv format for XLS2ExpressionMap

import re
import sys
import html
import itertools

from xml.etree import ElementTree

import constants
from .midi import mididata

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
        self.xmlRoot    = xmlTree.getroot()
        self.slot       = xmlRoot.find( "member[@name='slots']" )
        self.noteList   = []
        self.ccList     = []
        self.pcList     = []

    """
    deconvert
    """
    def deconvert( self ):

        if slot == None:
            return

        # <member name="slots">
        #     <int name="ownership" value="1"/>
        #     <list name="obj" type="obj">
        #         <obj class="PSoundSlot" ID="*****">  <-------- is i
        #         :
        #         :
        #         </obj>
        for i in self.slot.findall( "list/obj[@class='PSoundSlot']" ):
            pass

    def parseArticulationInfo( self ):
        # <member name="sv">
        # :
        # </member>

    def parseMidiEventInfo( elem ):
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
    pass
