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

.. _hosts:

======
 Hosts
======

Most resources that are referenced in an IT or cloud infrastructure are
conceptually "hosted on" or "hosted by" other resources. For example,
"applications" are hosted on "web servers" or "users" may be hosted on a
"network connected device" or a "terminal". In addition, networked resources
are "hosted" by some device attached to some network.

The host resource often provides context or location information for the
resource it is hosting at the time the Actual Event was observed and recorded
(e.g., an IP address, software agent, platform, etc.). Providing a means to
record host information with a CADF Event Record is valuable for audit purposes
because compliance policies and rules are often based on such information.

======== =============== ======== ==============================================
Property Type            Required Description
======== =============== ======== ==============================================
id       cadf:Identifier No       The optional identifier of the host RESOURCE
address  xs:anyURI       No       The optional address of the host RESOURCE
agent    xs:string       No       The optional agent (name) of the host RESOURCE
platform xs:string       No       The optional platform of the host RESOURCE
======== =============== ======== ==============================================

Serialisation
=============

json::

   {
    "id": "myuuid:1234-5678-90abc-defg-0000",
    "address": "10.0.2.15",
    "agent": "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:18.0)",
    "platform": "Linux version 3.5.0-23-generic (gcc version 4.6.3 (Ubuntu/Linaro 4.6.3-1ubuntu5) ) #35~precise1-Ubuntu SMP Fri Jan 25 17:15:33 UTC 2013"
   }

