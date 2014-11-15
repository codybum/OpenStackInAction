..
      Copyright 2014 IBM Corp

      Licensed under the Apache License, Version 2.0 (the "License"); you may
      not use this file except in compliance with the License. You may obtain
      a copy of the License at

          http://www.apache.org/licenses/LICENSE-2.0

      Unless required by applicable law or agreed to in writing, software
      distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
      WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
      License for the specific language governing permissions and limitations
      under the License.

.. _middleware:

=================
 Audit middleware
=================

The pyCADF library provides an optional WSGI middleware filter which allows
the ability to audit api requests for each component of OpenStack.

The audit middleware filter utilises environment variables to build the CADF
event.

.. figure:: ./images/middleware.png
   :figwidth: 100%
   :align: center
   :alt: Figure 1: Audit middleware in Nova pipeline

The figure above shows the middleware in Nova's pipeline.

Enabling audit middleware
=========================
To enable the audit middleware, the following requirements need to be
satisfied:

1. pyCADF library must be added to the requirements file of the project to be
   audited.

2. The project should utilise oslo.messaging_ notification system.

.. note::

   If the project utilises oslo's `old notification system`_, a compatible
   middleware can be synced from oslo-incubator's `middleware code base`_.

If the above requirements are satisfied, auditing can be enabled by editing
the project's api-paste.ini file to include the following filter definition:

::

   [filter:audit]
   paste.filter_factory = pycadf.middleware.audit:AuditMiddleware.factory

or

::

   [filter:audit]
   paste.filter_factory = <project>.openstack.common.middleware.audit:AuditMiddleware.factory

The filter should be included after Keystone's auth_token middleware so it can
utilise environment variables set by Keystone's middleware.  Below is an
example using Nova's WSGI pipeline::

   [composite:openstack_compute_api_v2]
   use = call:nova.api.auth:pipeline_factory
   noauth = faultwrap sizelimit noauth ratelimit osapi_compute_app_v2
   keystone = faultwrap sizelimit authtoken keystonecontext ratelimit audit osapi_compute_app_v2
   keystone_nolimit = faultwrap sizelimit authtoken keystonecontext audit osapi_compute_app_v2

.. _oslo.messaging: http://www.dmtf.org/standards/cadf
.. _old notification system: https://github.com/openstack/oslo-incubator
.. _middleware code base: https://github.com/openstack/oslo-incubator/tree/master/openstack/common/middleware

Configure audit middleware
==========================
To properly audit api requests, the audit middleware requires an
api_audit_map.conf to be defined. The project's corresponding
api_audit_map.conf file is included in the `pyCADF library`_.

By default, the audit middleware filter expects the map file to be located in
the same folder as the other conf files related to the project
(ie.'/etc/<project>' folder). This default functionality is to be deprecated
and so the location should be specified explicitly by adding the path to the
'audit_map_file' option of the filter definition::

   [filter:audit]
   paste.filter_factory = pycadf.middleware.audit:AuditMiddleware.factory
   audit_map_file = /etc/nova/api_audit_map.conf

Additional options can be set::

   [filter:audit]
   paste.filter_factory = pycadf.middleware.audit:AuditMiddleware.factory
   audit_map_file = /etc/nova/api_audit_map.conf
   service_name = test # opt to set HTTP_X_SERVICE_NAME environ variable
   ignore_req_list = GET,POST # opt to ignore specific requests

.. _pyCADF library: https://github.com/openstack/pycadf/tree/master/etc/pycadf
