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

.. _credentials:

============
 Credentials
============

This type provides a means to describe various credentials along with any
information about the authority that is responsible for maintaining them.
This is intended to be associated with a CADF Resource’s identity and reflects
any authorizations or identity assertions the resource may use to gain access
to other resources.

========== ========= ======== ===================================================================================================
Property   Type      Required Description
========== ========= ======== ===================================================================================================
type       xs:anyURI No       Type of credential. (e.g., auth. token, identity token, etc.)
token      xs:any    Yes      The primary opaque or non-opaque identity or security token (e.g., an opaque or obfuscated user ID)
authority  xs:anyURI No       The trusted authority (a service) that understands and can verify the credential.
assertions cadf:Map  No       Optional list of additional assertions or attributes that belong to the credential
========== ========= ======== ===================================================================================================

Serialisation
=============

json::

   {
    "typeURI": "http://schemas.dmtf.org/cloud/audit/1.0/event",
    "action": "authenticate",
    ...,
    "initiator": {
       "id": "joe.user@tenant1.com",
       "typeURI": "data/security/account/user",
       ...,
       "credential": {
          "type": "https://mycloud.com/v2/token",
          "token": "myuuid:1ef0-abdf-xxxx-xxxx"
       }
    }
   }

