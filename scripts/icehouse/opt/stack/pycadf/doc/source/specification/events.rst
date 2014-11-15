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

.. _events:

=======
 Events
=======

The CADF Event Model applies semantics to the activities, resources,
information, and changes within a cloud provider’s infrastructure and models
these using the concept of an event.

============= =================== ========= =============================================================================================================================================================
Property      Type                Required  Description
============= =================== ========= =============================================================================================================================================================
id            cadf:Identifier     Yes       The unique identifier of the CADF Event Record
typeURI       cadf:Path           Dependent Can be used to declare versioning of Events.
eventType     xs:string           Yes       The classification of the type of event
eventTime     cadf:Timestamp      Yes       The OBSERVER's best estimate as to the time the Actual Event occurred or began
action        cadf:Path           Yes       This property represents the event's ACTION
outcome       cadf:Path           Yes       A valid classification value from the CADF Outcome Taxonomy
initiator     cadf:Resource       Dependent The event's INITIATOR. Required if not initiatorId
initiatorId   cadf:Identifier     Dependent The event's INITIATOR resource by reference. Required if not initiator
target        cadf:Resource       Dependent The event's TARGET. Required if not targetId
targetId      cadf:Identifier     Dependent The event's TARGET by reference. Required if not target
observer      cadf:Resource       Dependent The event's OBSERVER. Required if not observerId
observerId    cadf:Identifier     Dependent The event's OBSERVER by reference. Required if not observer
reason        cadf:Reason         No        Domain-specific reason code and policy data that provides an additional level of detail to the outcome value. Required if the eventType property is "control"
severity      xs:string           No        Describes domain-relative severity assigned to the event by the OBSERVER. This property's value is non-normative
measurements  cadf:Measurement[]  Dependent Any measurement (values) associated with the event. Required if the eventType property is "monitor"
name          xs:string           No        A descriptive name for the event
tags          cadf:Tag[]          No        Array of Tags that MAY be used to further qualify or categorize the CADF Event Record
attachments   cadf:Attachment[]   No        Array of extended or domain-specific information about the event or its context
reporterchain cadf:Reporterstep[] No        Array of Reporterstep typed data that contains information about the sequenced handling of or change to the associated CADF Event Record by any REPORTER
============= =================== ========= =============================================================================================================================================================

Serialisation
=============

json::

   {
    'typeURI': 'http://schemas.dmtf.org/cloud/audit/1.0/event',
    'id': 'openstack:a80dc5ee-be83-48ad-ad5e-6577f2217637‘,
    'eventType': 'activity',
    'action': 'read',
    'outcome': 'success',
    'reason': {'reasonCode': '200', 'reasonType': 'HTTP'},
    'eventTime': '2014-01-17T23:23:38.109989+0000',
    'initiator': {
          'id': 'openstack:95f12d248a234a969f456cd2c794f29a'
          'typeURI': 'service/security/account/user',
          'name': ‘admin',
          'project_id': 'openstack:e55b158759854ea6a7852aa76632c6c1',
          'credential': {
                   'token': ‘MIIQBgYJKoZIhvcNAQcCoIIP9z xxxxxx KoZIhvcIP9z=‘,
                   'identity_status': 'Confirmed'},
          'host': {
                   'agent': 'python-novaclient',
                   'address': '9.26.27.109'},
    },
    'target': {
         'id': 'openstack:0f126160203748a5b4923f2eb6e3b7db',
         'typeURI': ‘service/compute/servers',
         'name': 'nova‘
         'addresses': [
              {'url': 'http://9.26.27.109:8774/v2/e55b158759854ea6a7852aa76632c6c1',
               'name': 'admin'},
              {'url': 'http://9.26.27.109:8774/v2/e55b158759854ea6a7852aa76632c6c1',
               'name': 'private'},
              {'url': 'http://9.26.27.109:8774/v2/e55b158759854ea6a7852aa76632c6c1',
               'name': 'public'}
          ],
    },
    'observer': { 'id': 'target'},
    'reporterchain': [
         {'reporterTime': '2014-01-17T23:23:38.154152+0000',
          'role': 'modifier',
          'reporter': {'id': 'target'}}
     ],
    'requestPath': '/v2/56600971-90f3-4370-807f-ab79339381a9/servers',
    'tags': ['correlation_id?value=openstack:bcac04dc-e0be-4110-862c-347088a7836a']
   }
