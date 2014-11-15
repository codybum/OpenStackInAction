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

.. _measurements:

=============
 Measurements
=============

A component that contains statistical or measurement information for TARGET
resources that are being monitored. The measurement should be based upon a
defined metric (a method of measurement).

============ =============== ========= =================================================================================================================
Property     Type            Required  Description
============ =============== ========= =================================================================================================================
result       xs:any          Yes       The quantitative or qualitative result of a measurement from applying the associated metric
metric       cadf:Metric     Dependent The property describes the metric used in generating the measurement result. Required if not metricId
metricId     cadf:Identifier Dependent This property identifies a CADF Metric by reference and whose definition exists elsewhere. Required if not metric
calculatedBy cadf:Resource   No        An optional description of the resource that calculated the measurement
============ =============== ========= =================================================================================================================

Metrics
=======

The Metric data type describes the rules and processes for measuring some
activity or resource, resulting in the generation of some values (captured by
the Measurement type).

=========== =============== ======== ==================================================
Property    Type            Required Description
=========== =============== ======== ==================================================
metricId    cadf:identifier Yes      The identifier for the metric.
unit        xs:string       Yes      The metrics unit (e.g., "ms", "Hz", "GB", etc.)
name        xs:string       No       A descriptive name for metric
annotations cadf:map        No       User-defined metric information.
=========== =============== ======== ==================================================

Serialisation
=============

json::

   {
    "typeURI": "http://schemas.dmtf.org/cloud/audit/1.0/log",
    ...,
    "metrics": [
    {
     "metricId": "myuuid://metric.org/1234",
     "unit": "GB",
     "name": "Storage Capacity in Gigabytes"
    }],
    ...,
    "events": [
    {
     "typeURI": "http://schemas.dmtf.org/cloud/audit/1.0/event",
     ...,
     "measurements": [
     {
      "result": "10",
      "metricId": "myuuid://metric.org/1234"
     }],
     ...
     }]
    }
