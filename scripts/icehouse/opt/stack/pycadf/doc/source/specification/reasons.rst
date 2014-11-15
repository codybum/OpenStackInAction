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

.. _reasons:

========
 Reasons
========

A component that contains a means to provide additional details and further
classify the top-level OUTCOME of the ACTION included in a CADF Event Record.

========== ========= ======== =====================================================================================================================
Property   Type      Required Description
========== ========= ======== =====================================================================================================================
reasonType xs:anyURI No       The domain URI that defines the "reasonCode" property's value
reasonCode xs:string No       An optional detailed result code as described by the domain identified in the "reasonType" property
policyType xs:anyURI No       The domain URI that defines the "policyId" property’s value
policyId   xs:string No       An optional identifier that indicates which policy or algorithm was applied in order to achieve the described OUTCOME
========== ========= ======== =====================================================================================================================

Serialisation
=============

json::

   {
    "typeURI": "http://schemas.dmtf.org/cloud/audit/1.0/event",
    ...,
    "reason": {
               "reasonType": "http://www.iana.org/assignments/http-status-codes/http-status-codes.xml",
               "reasonCode": "408",
               "policyType": "http://schemas.xmlsoap.org/ws/2002/12/policy",
               "policyId": "http://10.0.3.4/firewall-ruleset/rule0012"
    },
    ...
   }
