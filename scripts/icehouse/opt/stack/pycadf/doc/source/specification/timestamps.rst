..
      Copyright 2014 IBM Corp.

      Licensed under the Apache License, Version 2.0 (the "License"); you may
      not use this file except in compliance with the License. You may obtain
      a copy of the License at

          http://www.apache.org/licenses/LICENSE-2.0

      Unless required by applicable law or agreed to in writing, software
      distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
      WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
      License for the specific language governing permissions and limitations
      under the License.

.. _timestamps:

===========
 Timestamps
===========

The following example shows the required Lexical representation of the
Timestamp type used in this specification; all Timestamp typed values
SHALL be formatted accordingly:

::

   yyyy '-' mm '-' dd 'T' hh ':' mm ':' ss ('.' s+)('+' | '-') hh ':' mm

.. note::

   The UTC offset is always required (not optional) and the use of the
   character 'Z' (or 'Zulu' time) as an abbreviation for UTC offset +00:00
   or -00:00 is NOT permitted.