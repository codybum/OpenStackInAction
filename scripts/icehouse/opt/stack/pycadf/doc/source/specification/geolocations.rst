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

.. _geolocations:

=============
 Geolocations
=============

Geolocation information, which reveals a resource’s physical location, is
obtained by using tracking technologies such as global positioning system
(GPS) devices, or IP geolocation by using databases that map IP addresses to
geographic locations. Geolocation information is widely used in
context-sensitive content delivery, enforcing location-based access
restrictions on services, and fraud detection and prevention.

Due to the intense concerns about security and privacy, countries and regions
introduced various legislation and regulation. To determine whether an event
is compliant sometimes depends on the geolocation of the event. Therefore, it
is crucial to report geolocation information unambiguously in an audit trail.

=========== ========= ======== ===============================================================================================================
Property    Type      Required Description
=========== ========= ======== ===============================================================================================================
id          xs:anyURI No       Optional identifier for a geolocation
latitude    xs:string No       The latitude of a geolocation
longitude   xs:string No       The longitude of a geolocation
elevation   xs:double No       The elevation of a geolocation in meters
accuracy    xs:double No       The accuracy of a geolocation in meters
city        xs:string No       The city of a geolocation
state       xs:string No       The state/province of a geolocation
regionICANN xs:string No       A region (e.g., a country, a sovereign state, a dependent territory or a special area of geographical interest)
annotations cadf:Map  No       User-defined geolocation information (e.g., building name, room number)
=========== ========= ======== ===============================================================================================================

Usage Requirements
==================
1. Geolocation typed data SHALL contain at least one valid property and
   associated value.

2. Geolocation typed data SHALL NOT be used to represent virtual or logical
   locations (e.g. network zone).

3. For each geolocation data instance, the properties SHALL be consistent.
   That is, all properties SHALL consistently represent the same geographic
   location and SHALL NOT provide conflicting value data.

::

   Example: ‘latitude’, ‘longitude’ and ‘region’ are all supplied as
   properties describing the same geolocation, the 'latitude' and
   'longitude' properties' coordinate values should resolve to the
   same geographic location as described by the 'region'
   property's value.

4. ICANN's implementation plan states "Upper and lower case characters are
   considered to be syntactically and semantically identical"; therefore,
   the "regionICANN" property's values MAY be either upper or lower case.

Serialisation
=============

json::

   {
    "typeURI": "http://schemas.dmtf.org/cloud/audit/1.0/event",
    ...,
    "target": {
               ...,
               "geolocation": {
                               "latitude": "+372207.90",
                               "longitude": "-1220210.20",
                               "elevation": "10"
               }
    }
   }
