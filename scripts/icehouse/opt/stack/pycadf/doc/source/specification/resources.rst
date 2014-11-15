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

.. _resources:

==========
 Resources
==========

Resources in general can be used to describe traditional IT components
(e.g., servers, network devices, etc.), software components
(e.g., platforms, databases, applications, etc.), operational and business
data (e.g., accounts, users, etc.) and roles, which can be assigned to
persons, that describe the authority to access capabilities.

============= ================= ========= ===================================================================================================================================
Property      Type              Required  Description
============= ================= ========= ===================================================================================================================================
id            cadf:Identifier   Yes       The identifier for the resource
typeURI       cadf:Path         Yes       The classification (i.e., type) of the resource using the CADF Resource Taxonomy
name          xs:string         No        The optional local name for the resource (not necessarily unique)
domain        xs:string         No        The optional name of the domain that qualifies the name of the resource
credential    cadf:Credential   No        The optional security credentials associated with the resource’s identity
addresses     cadf:Endpoint[]   No        The optional descriptive addresses (including URLs) of the resource
host          cadf:Host         No        The optional information about the (network) host of the resource
geolocation   cadf:Geolocation  Dependent This optional property describes the geographic location of the resource using Geolocation data type. Required if not geolocationId
geolocationId cadf:Identifier   Dependent This optional property identifies a CADF Geolocation by reference. Required if not geolocation
attachments   cadf:Attachment[] No        An optional array of extended or domain-specific information about the resource or its contex
============= ================= ========= ===================================================================================================================================

Serialisation
=============

json::

   {
    "typeURI": "http://schemas.dmtf.org/cloud/audit/1.0/event",
    ...,
    "target": {
               "id": "myscheme://mydomain/resource/id/0001",
               "typeURI": "service/compute",
               "name": "server_0001",
               ...,
               "geolocation": {
                               "city": "Austin",
                               "state": "TX",
                               "regionICANN": "US"
               }
    }
   }


