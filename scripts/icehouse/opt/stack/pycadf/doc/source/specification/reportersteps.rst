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

.. _reportersteps:

==============
 Reportersteps
==============

This type represents a step in the REPORTERCHAIN that captures information
about any notable REPORTER (in addition to the OBSERVER) that modified or
relayed the CADF Event Record and any details regarding any modification it
performed on the CADF Event Record it is contained within.

The Reporterstep data type should capture information about the resources that
have had a role in modifying, or relaying the CADF Event Record during its
lifecycle after having been created by the OBSERVER.

============ ================= ========= ==========================================================================================================================
Property     Type              Required  Description
============ ================= ========= ==========================================================================================================================
role         xs:string         Yes       The role the REPORTER performed on the CADF Event Record (e.g., an "observer", "modifier" or "relay" role)
reporter     cadf:Resource     Dependent This property defines the resource that acted as a REPORTER on a CADF Event Record. Required if not reporterId
reporterId   cadf:Identifier   Dependent This property identifies a resource that acted as a REPORTER on a CADF Event Record by reference. Required if not reporter
reporterTime cadf:Timestamp    No        The time a REPORTER adds its Reporterstep entry into the REPORTERCHAIN
attachments  cadf:Attachment[] No        An optional array of additional data containing information about the reporter or any action it performed
============ ================= ========= ==========================================================================================================================

Serialisation
=============

json::

   {
    "typeURI": "http://schemas.dmtf.org/cloud/audit/1.0/event",
    ...,
    "reporterchain": [
    {
     "role": "modifier",
     "reporterTime": "2012-03-22T13:00:00-04:00",
     "reporter": {
                  "id": "myscheme://mydomain/resource/monitor/id/0002"
     }
    },
    ...
    ]
   }

