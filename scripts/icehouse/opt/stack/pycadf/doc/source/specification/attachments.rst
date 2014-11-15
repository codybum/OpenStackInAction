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

.. _attachments:

============
 Attachments
============

An attachment is a container for data or "content" that may follow any
structure – from an atomic type to a complex hierarchy. However, it is
desirable for processing and interoperability that the type – or
structure – of the content be identified by a simple value. To this end the
attachment also contains a "content type", i.e., a URI that identifies the
kind of content.

Attachments are intended to be used for inclusion of domain-specific,
informative, or descriptive information.

=========== ========= ======== ======================================================================================
Property    Type      Required Description
=========== ========= ======== ======================================================================================
typeURI     xs:anyURI Yes      The URI that identifies the type of data contained in the "content" property.
content     xs:any    Yes      A container that contains any type of data (as defined by the "contentType" property).
contentType xs:string Yes      An optional name that can be used to provide an identifying name for the content.
=========== ========= ======== ======================================================================================

Serialisation
=============

json::

   {
    ...,
    "attachments": [
    {
     "content": "xs:any",
     "contentType": "xs:anyURI"
    },
    {
     "content": "xs:any",
     "contentType": "xs:anyURI"
    }
    ]
   }

