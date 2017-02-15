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

XML_HEADER = """<?xml version="1.0" encoding="utf-8"?>
<InstrumentMap>
<string name="name" value="VHG Mono (Main)" wide="true"/>
"""

XML_FOOTER = """   <member name="controller">
      <int name="ownership" value="1"/>
   </member>
</InstrumentMap>
"""


SLOTS_HEADER = """
   <member name="slots">
      <int name="ownership" value="1"/>
      <list name="obj" type="obj">
         <obj class="PSoundSlot" ID="{uuid1}">
            <obj class="PSlotThruTrigger" name="remote" ID="{uuid2}">
               <int name="status" value="144"/>
               <int name="data1" value="-1"/>
            </obj>
"""

PSlotMidiAction = """
            <obj class="PSlotMidiAction" name="action" ID="{uuid1}">
               <int name="version" value="600"/>
               <member name="noteChanger">
                  <int name="ownership" value="1"/>
                  <list name="obj" type="obj">
                     <obj class="PSlotNoteChanger" ID="{uuid2}">
                        <int name="channel" value="-1"/>
                        <float name="velocityFact" value="1"/>
                        <float name="lengthFact" value="1"/>
                        <int name="minVelocity" value="0"/>
                        <int name="maxVelocity" value="127"/>
                        <int name="transpose" value="0"/>
                        <int name="minPitch" value="0"/>
                        <int name="maxPitch" value="127"/>
                     </obj>
                  </list>
               </member>
               <member name="midiMessages">
                  <int name="ownership" value="1"/>
                  <list name="obj" type="obj">
                     <obj class="POutputEvent" ID="{uuid3}">
                        <int name="status" value="144"/>
                        <int name="data1" value="{note}"/>
                        <int name="data2" value="120"/>
                     </obj>
                  </list>
               </member>
               <int name="channel" value="-1"/>
               <float name="velocityFact" value="1"/>
               <float name="lengthFact" value="1"/>
               <int name="minVelocity" value="0"/>
               <int name="maxVelocity" value="127"/>
               <int name="transpose" value="0"/>
               <int name="maxPitch" value="127"/>
               <int name="minPitch" value="0"/>
               <int name="key" value="0"/>
            </obj>
            <member name="sv">
               <int name="ownership" value="2"/>
            </member>
            <member name="name">
               <string name="s" value="{name}" wide="true"/>
            </member>
            <int name="color" value="{color}"/>

"""

SLOTS_FOOTER = """
         </obj>
"""

ARTICULATION = """
         <obj class="USlotVisuals" ID="{uuid}">
            <int name="displaytype" value="1"/>
            <int name="articulationtype" value="1"/>
            <int name="symbol" value="73"/>
            <string name="text" value="{name}" wide="true"/>
            <string name="description" value="{name}" wide="true"/>
            <int name="group" value="0"/>
         </obj>
"""
