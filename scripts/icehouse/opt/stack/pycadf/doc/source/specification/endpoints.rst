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

.. _endpoints:

==========
 Endpoints
==========

The Endpoint type is used to provide information about a resource's location
on a network.

======== ========= ======== =================================================================================
Property Type      Required Description
======== ========= ======== =================================================================================
url      xs:anyURI Yes      The network address of the endpoint; for IP-based addresses
name     xs:string No       An optional property to provide a logical name for the endpoint
port     xs:string No       An optional property to provide the port value separate from the address property
======== ========= ======== =================================================================================

Serialisation
=============

json::

   {
    "typeURI": "http://schemas.dmtf.org/cloud/audit/1.0/event",
    ...,
    "target": {
       "id": "myscheme://mydomain/resource/id/0001",
       "name": "server_0001",
       "addresses": [{
           "name": "public",
           "url": "http://mydomain/mypath/server-0001/"
        },
       ...
       ],
       ...
    }
   }

