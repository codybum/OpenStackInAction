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

.. _taxonomy:

=========
 Taxonomy
=========

The CADF Resource Taxonomy describes resources that are commonly used in cloud
and enterprise infrastructures. This list was developed based on surveys of
existing cloud architectures, deployments, and implementations. The Resource
Taxonomy, however, is fully intended to be extensible by profiles that may
define additional resource nodes as child nodes to the ones specified below.
When doing so, however, vendors and cloud providers should be aware that this
places an additional burden on the consumer to correctly comprehend the new
node type. Therefore, vendors and providers of CADF audit data should be
careful to provide classification values that extend the existing tree from the
most granular node that closely matches the functions of any newly-defined
resource types. This approach will provide consumers with a baseline
understanding of the function of the new resource type.