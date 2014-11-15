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

.. _identifiers:

============
 Identifiers
============

This specification defines an Identifier type that is based upon the Uniform
Resource Identifier Reference (URI) as specified in RFC3986. Any value that
represents a CADF Identifier type in this specification, its extensions, or
profiles SHALL adhere to the requirements listed in this section:

.. note::

   CADF Identifier type values SHALL be created to be Universally Unique
   Identifiers (UUIDs) so that when CADF data (e.g., CADF Event Records, Logs,
   Reports, Resources, Metrics, etc.) are federated it will be uniquely
   identifiable to the source (e.g., cloud provider, service, etc.) that
   created them.
