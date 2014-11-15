# Copyright 2013 IBM Corp.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy of
# the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.

import uuid

from oslo.config import cfg
import webob

from pycadf.audit import api
from pycadf.tests import base


class TestAuditApi(base.TestCase):
    ENV_HEADERS = {'HTTP_X_SERVICE_CATALOG':
                   '''[{"endpoints_links": [],
                        "endpoints": [{"adminURL":
                                       "http://admin_host:8774",
                                       "region": "RegionOne",
                                       "publicURL":
                                       "http://public_host:8775",
                                       "internalURL":
                                       "http://internal_host:8776",
                                       "id": "resource_id"}],
                        "type": "compute",
                        "name": "nova"},]''',
                   'HTTP_X_USER_ID': 'user_id',
                   'HTTP_X_USER_NAME': 'user_name',
                   'HTTP_X_AUTH_TOKEN': 'token',
                   'HTTP_X_PROJECT_ID': 'tenant_id',
                   'HTTP_X_IDENTITY_STATUS': 'Confirmed'}

    def setUp(self):
        super(TestAuditApi, self).setUp()
        self.audit_api = api.OpenStackAuditApi(
            'etc/pycadf/nova_api_audit_map.conf')

    def api_request(self, method, url):
        self.ENV_HEADERS['REQUEST_METHOD'] = method
        req = webob.Request.blank(url, environ=self.ENV_HEADERS,
                                  remote_addr='192.168.0.1')
        self.audit_api.append_audit_event(req)
        self.assertIn('CADF_EVENT_CORRELATION_ID', req.environ)
        return req

    def test_get_list_with_cfg(self):
        cfg.CONF.set_override(
            'api_audit_map',
            self.path_get('etc/pycadf/nova_api_audit_map.conf'),
            group='audit')
        self.audit_api = api.OpenStackAuditApi()
        req = self.api_request('GET',
                               'http://admin_host:8774/v2/'
                               + str(uuid.uuid4()) + '/servers/')
        payload = req.environ['CADF_EVENT']
        self.assertEqual(payload['action'], 'read/list')

    def test_get_list(self):
        req = self.api_request('GET', 'http://admin_host:8774/v2/'
                               + str(uuid.uuid4()) + '/servers')
        payload = req.environ['CADF_EVENT']
        self.assertEqual(payload['action'], 'read/list')
        self.assertEqual(payload['typeURI'],
                         'http://schemas.dmtf.org/cloud/audit/1.0/event')
        self.assertEqual(payload['outcome'], 'pending')
        self.assertEqual(payload['eventType'], 'activity')
        self.assertEqual(payload['target']['name'], 'nova')
        self.assertEqual(payload['target']['id'], 'openstack:resource_id')
        self.assertEqual(payload['target']['typeURI'],
                         'service/compute/servers')
        self.assertEqual(len(payload['target']['addresses']), 3)
        self.assertEqual(payload['target']['addresses'][0]['name'], 'admin')
        self.assertEqual(payload['target']['addresses'][0]['url'],
                         'http://admin_host:8774')
        self.assertEqual(payload['initiator']['id'], 'openstack:user_id')
        self.assertEqual(payload['initiator']['name'], 'user_name')
        self.assertEqual(payload['initiator']['project_id'],
                         'openstack:tenant_id')
        self.assertEqual(payload['initiator']['host']['address'],
                         '192.168.0.1')
        self.assertEqual(payload['initiator']['typeURI'],
                         'service/security/account/user')
        self.assertNotEqual(payload['initiator']['credential']['token'],
                            'token')
        self.assertEqual(payload['initiator']['credential']['identity_status'],
                         'Confirmed')
        self.assertNotIn('reason', payload)
        self.assertNotIn('reporterchain', payload)
        self.assertEqual(payload['observer']['id'], 'target')
        self.assertEqual(req.path, payload['requestPath'])

    def test_get_read(self):
        req = self.api_request('GET',
                               'http://admin_host:8774/v2/'
                               + str(uuid.uuid4()) + '/servers/'
                               + str(uuid.uuid4()))
        payload = req.environ['CADF_EVENT']
        self.assertEqual(payload['target']['typeURI'],
                         'service/compute/servers/server')
        self.assertEqual(payload['action'], 'read')
        self.assertEqual(payload['outcome'], 'pending')

    def test_get_unknown_endpoint(self):
        req = self.api_request('GET',
                               'http://unknown:8774/v2/'
                               + str(uuid.uuid4()) + '/servers')
        payload = req.environ['CADF_EVENT']
        self.assertEqual(payload['action'], 'read/list')
        self.assertEqual(payload['outcome'], 'pending')
        self.assertEqual(payload['target']['name'], 'unknown')
        self.assertEqual(payload['target']['id'], 'unknown')
        self.assertEqual(payload['target']['typeURI'], 'unknown')

    def test_get_unknown_endpoint_default_set(self):
        tmpfile = self.temp_config_file_path()
        with open(tmpfile, "w") as f:
            f.write("[DEFAULT]\n")
            f.write("target_endpoint_type = compute \n")
            f.write("[path_keywords]\n")
            f.write("servers = server\n\n")
            f.write("[service_endpoints]\n")
            f.write("compute = service/compute")
        self.audit_api = api.OpenStackAuditApi(tmpfile)

        req = self.api_request('GET',
                               'http://unknown:8774/v2/'
                               + str(uuid.uuid4()) + '/servers')
        self.assertEqual(self.audit_api._MAP.default_target_endpoint_type,
                         'compute')
        payload = req.environ['CADF_EVENT']
        self.assertEqual(payload['action'], 'read/list')
        self.assertEqual(payload['outcome'], 'pending')
        self.assertEqual(payload['target']['name'], 'nova')
        self.assertEqual(payload['target']['id'], 'openstack:resource_id')
        self.assertEqual(payload['target']['typeURI'],
                         'service/compute/servers')

    def test_put(self):
        req = self.api_request('PUT', 'http://admin_host:8774/v2/'
                               + str(uuid.uuid4()) + '/servers')
        payload = req.environ['CADF_EVENT']
        self.assertEqual(payload['target']['typeURI'],
                         'service/compute/servers')
        self.assertEqual(payload['action'], 'update')
        self.assertEqual(payload['outcome'], 'pending')

    def test_delete(self):
        req = self.api_request('DELETE', 'http://admin_host:8774/v2/'
                               + str(uuid.uuid4()) + '/servers')
        payload = req.environ['CADF_EVENT']
        self.assertEqual(payload['target']['typeURI'],
                         'service/compute/servers')
        self.assertEqual(payload['action'], 'delete')
        self.assertEqual(payload['outcome'], 'pending')

    def test_head(self):
        req = self.api_request('HEAD', 'http://admin_host:8774/v2/'
                               + str(uuid.uuid4()) + '/servers')
        payload = req.environ['CADF_EVENT']
        self.assertEqual(payload['target']['typeURI'],
                         'service/compute/servers')
        self.assertEqual(payload['action'], 'read')
        self.assertEqual(payload['outcome'], 'pending')

    def test_post_update(self):
        req = self.api_request('POST',
                               'http://admin_host:8774/v2/'
                               + str(uuid.uuid4()) + '/servers/'
                               + str(uuid.uuid4()))
        payload = req.environ['CADF_EVENT']
        self.assertEqual(payload['target']['typeURI'],
                         'service/compute/servers/server')
        self.assertEqual(payload['action'], 'update')
        self.assertEqual(payload['outcome'], 'pending')

    def test_post_create(self):
        req = self.api_request('POST', 'http://admin_host:8774/v2/'
                               + str(uuid.uuid4()) + '/servers')
        payload = req.environ['CADF_EVENT']
        self.assertEqual(payload['target']['typeURI'],
                         'service/compute/servers')
        self.assertEqual(payload['action'], 'create')
        self.assertEqual(payload['outcome'], 'pending')

    def test_post_action(self):
        self.ENV_HEADERS['REQUEST_METHOD'] = 'POST'
        req = webob.Request.blank('http://admin_host:8774/v2/'
                                  + str(uuid.uuid4()) + '/servers/action',
                                  environ=self.ENV_HEADERS)
        req.body = b'{"createImage" : {"name" : "new-image","metadata": ' \
                   b'{"ImageType": "Gold","ImageVersion": "2.0"}}}'
        self.audit_api.append_audit_event(req)
        payload = req.environ['CADF_EVENT']
        self.assertEqual(payload['target']['typeURI'],
                         'service/compute/servers/action')
        self.assertEqual(payload['action'], 'update/createImage')
        self.assertEqual(payload['outcome'], 'pending')

    def test_post_empty_body_action(self):
        self.ENV_HEADERS['REQUEST_METHOD'] = 'POST'
        req = webob.Request.blank('http://admin_host:8774/v2/'
                                  + str(uuid.uuid4()) + '/servers/action',
                                  environ=self.ENV_HEADERS)
        self.audit_api.append_audit_event(req)
        payload = req.environ['CADF_EVENT']
        self.assertEqual(payload['target']['typeURI'],
                         'service/compute/servers/action')
        self.assertEqual(payload['action'], 'create')
        self.assertEqual(payload['outcome'], 'pending')

    def test_custom_action(self):
        req = self.api_request('GET', 'http://admin_host:8774/v2/'
                               + str(uuid.uuid4()) + '/os-hosts/'
                               + str(uuid.uuid4()) + '/reboot')
        payload = req.environ['CADF_EVENT']
        self.assertEqual(payload['target']['typeURI'],
                         'service/compute/os-hosts/host/reboot')
        self.assertEqual(payload['action'], 'start/reboot')
        self.assertEqual(payload['outcome'], 'pending')

    def test_custom_action_complex(self):
        req = self.api_request('GET', 'http://admin_host:8774/v2/'
                               + str(uuid.uuid4()) + '/os-migrations')
        payload = req.environ['CADF_EVENT']
        self.assertEqual(payload['target']['typeURI'],
                         'service/compute/os-migrations')
        self.assertEqual(payload['action'], 'read')
        req = self.api_request('POST', 'http://admin_host:8774/v2/'
                               + str(uuid.uuid4()) + '/os-migrations')
        payload = req.environ['CADF_EVENT']
        self.assertEqual(payload['target']['typeURI'],
                         'service/compute/os-migrations')
        self.assertEqual(payload['action'], 'create')

    def test_response_mod_msg(self):
        req = self.api_request('GET', 'http://admin_host:8774/v2/'
                               + str(uuid.uuid4()) + '/servers')
        payload = req.environ['CADF_EVENT']
        self.audit_api.mod_audit_event(req, webob.Response())
        payload2 = req.environ['CADF_EVENT']
        self.assertEqual(payload['id'], payload2['id'])
        self.assertEqual(payload['tags'], payload2['tags'])
        self.assertEqual(payload2['outcome'], 'success')
        self.assertEqual(payload2['reason']['reasonType'], 'HTTP')
        self.assertEqual(payload2['reason']['reasonCode'], '200')
        self.assertEqual(len(payload2['reporterchain']), 1)
        self.assertEqual(payload2['reporterchain'][0]['role'], 'modifier')
        self.assertEqual(payload2['reporterchain'][0]['reporter']['id'],
                         'target')

    def test_no_response(self):
        req = self.api_request('GET', 'http://admin_host:8774/v2/'
                               + str(uuid.uuid4()) + '/servers')
        payload = req.environ['CADF_EVENT']
        self.audit_api.mod_audit_event(req, None)
        payload2 = req.environ['CADF_EVENT']
        self.assertEqual(payload['id'], payload2['id'])
        self.assertEqual(payload['tags'], payload2['tags'])
        self.assertEqual(payload2['outcome'], 'unknown')
        self.assertNotIn('reason', payload2)
        self.assertEqual(len(payload2['reporterchain']), 1)
        self.assertEqual(payload2['reporterchain'][0]['role'], 'modifier')
        self.assertEqual(payload2['reporterchain'][0]['reporter']['id'],
                         'target')

    def test_missing_req(self):
        self.ENV_HEADERS['REQUEST_METHOD'] = 'GET'
        req = webob.Request.blank('http://admin_host:8774/v2/'
                                  + str(uuid.uuid4()) + '/servers',
                                  environ=self.ENV_HEADERS)
        self.assertNotIn('CADF_EVENT', req.environ)
        self.audit_api.mod_audit_event(req, webob.Response())
        self.assertIn('CADF_EVENT', req.environ)
        self.assertIn('CADF_EVENT_CORRELATION_ID', req.environ)
        payload = req.environ['CADF_EVENT']
        self.assertEqual(payload['outcome'], 'success')
        self.assertEqual(payload['reason']['reasonType'], 'HTTP')
        self.assertEqual(payload['reason']['reasonCode'], '200')
        self.assertEqual(payload['observer']['id'], 'target')
        self.assertNotIn('reporterchain', payload)


class TestAuditApiConf(base.TestCase):
    def test_missing_default_option(self):
        tmpfile = self.temp_config_file_path()
        # NOTE(gordc): ensure target_endpoint_type is not in conf file
        with open(tmpfile, "w") as f:
            f.write("[DEFAULT]\n")
            f.write("api_paths = servers\n\n")
            f.write("[service_endpoints]\n")
            f.write("compute = service/compute")
        self.audit_api = api.OpenStackAuditApi(tmpfile)
