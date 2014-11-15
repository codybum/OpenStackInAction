# Copyright 2013 OpenStack LLC
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

import time

from pycadf import attachment
from pycadf import credential
from pycadf import endpoint
from pycadf import event
from pycadf import geolocation
from pycadf import host
from pycadf import identifier
from pycadf import measurement
from pycadf import metric
from pycadf import reason
from pycadf import reporterstep
from pycadf import resource
from pycadf import tag
from pycadf.tests import base
from pycadf import timestamp


class TestCADFSpec(base.TestCase):
    def test_endpoint(self):
        endp = endpoint.Endpoint(url='http://192.168.0.1',
                                 name='endpoint name',
                                 port='8080')
        self.assertEqual(endp.is_valid(), True)
        dict_endp = endp.as_dict()
        for key in endpoint.ENDPOINT_KEYNAMES:
            self.assertIn(key, dict_endp)

    def test_host(self):
        h = host.Host(id=identifier.generate_uuid(),
                      address='192.168.0.1',
                      agent='client',
                      platform='AIX')
        self.assertEqual(h.is_valid(), True)
        dict_host = h.as_dict()
        for key in host.HOST_KEYNAMES:
            self.assertIn(key, dict_host)

    def test_credential(self):
        cred = credential.Credential(type='auth token',
                                     token=identifier.generate_uuid())
        self.assertEqual(cred.is_valid(), True)
        dict_cred = cred.as_dict()
        for key in credential.CRED_KEYNAMES:
            self.assertIn(key, dict_cred)

    def test_federated_credential(self):
        cred = credential.FederatedCredential(
            token=identifier.generate_uuid(),
            type='http://docs.oasis-open.org/security/saml/v2.0',
            identity_provider=identifier.generate_uuid(),
            user=identifier.generate_uuid(),
            groups=[
                identifier.generate_uuid(),
                identifier.generate_uuid(),
                identifier.generate_uuid()])
        self.assertEqual(cred.is_valid(), True)
        dict_cred = cred.as_dict()
        for key in credential.FED_CRED_KEYNAMES:
            self.assertIn(key, dict_cred)

    def test_geolocation(self):
        geo = geolocation.Geolocation(id=identifier.generate_uuid(),
                                      latitude='43.6481 N',
                                      longitude='79.4042 W',
                                      elevation='0',
                                      accuracy='1',
                                      city='toronto',
                                      state='ontario',
                                      regionICANN='ca')
        self.assertEqual(geo.is_valid(), True)

        dict_geo = geo.as_dict()
        for key in geolocation.GEO_KEYNAMES:
            self.assertIn(key, dict_geo)

    def test_metric(self):
        metric_val = metric.Metric(metricId=identifier.generate_uuid(),
                                   unit='b',
                                   name='bytes')
        self.assertEqual(metric_val.is_valid(), True)

        dict_metric_val = metric_val.as_dict()
        for key in metric.METRIC_KEYNAMES:
            self.assertIn(key, dict_metric_val)

    def test_measurement(self):
        measure_val = measurement.Measurement(
            result='100',
            metric=metric.Metric(),
            metricId=identifier.generate_uuid(),
            calculatedBy=resource.Resource(typeURI='storage'))
        self.assertEqual(measure_val.is_valid(), False)

        dict_measure_val = measure_val.as_dict()
        for key in measurement.MEASUREMENT_KEYNAMES:
            self.assertIn(key, dict_measure_val)

        measure_val = measurement.Measurement(
            result='100',
            metric=metric.Metric(),
            calculatedBy=resource.Resource(typeURI='storage'))
        self.assertEqual(measure_val.is_valid(), True)

        measure_val = measurement.Measurement(
            result='100',
            metricId=identifier.generate_uuid(),
            calculatedBy=resource.Resource(typeURI='storage'))
        self.assertEqual(measure_val.is_valid(), True)

    def test_reason(self):
        reason_val = reason.Reason(reasonType='HTTP',
                                   reasonCode='200',
                                   policyType='poltype',
                                   policyId=identifier.generate_uuid())
        self.assertEqual(reason_val.is_valid(), True)

        dict_reason_val = reason_val.as_dict()
        for key in reason.REASON_KEYNAMES:
            self.assertIn(key, dict_reason_val)

    def test_reporterstep(self):
        step = reporterstep.Reporterstep(
            role='modifier',
            reporter=resource.Resource(typeURI='storage'),
            reporterId=identifier.generate_uuid(),
            reporterTime=timestamp.get_utc_now())
        self.assertEqual(step.is_valid(), False)

        dict_step = step.as_dict()
        for key in reporterstep.REPORTERSTEP_KEYNAMES:
            self.assertIn(key, dict_step)

        step = reporterstep.Reporterstep(
            role='modifier',
            reporter=resource.Resource(typeURI='storage'),
            reporterTime=timestamp.get_utc_now())
        self.assertEqual(step.is_valid(), True)

        step = reporterstep.Reporterstep(
            role='modifier',
            reporterId=identifier.generate_uuid(),
            reporterTime=timestamp.get_utc_now())
        self.assertEqual(step.is_valid(), True)

    def test_attachment(self):
        attach = attachment.Attachment(typeURI='attachURI',
                                       content='content',
                                       name='attachment_name')
        self.assertEqual(attach.is_valid(), True)

        dict_attach = attach.as_dict()
        for key in attachment.ATTACHMENT_KEYNAMES:
            self.assertIn(key, dict_attach)

    def test_resource(self):
        res = resource.Resource(typeURI='storage',
                                name='res_name',
                                domain='res_domain',
                                ref='res_ref',
                                credential=credential.Credential(
                                    token=identifier.generate_uuid()),
                                host=host.Host(address='192.168.0.1'),
                                geolocation=geolocation.Geolocation(),
                                geolocationId=identifier.generate_uuid())

        res.add_attachment(attachment.Attachment(typeURI='attachURI',
                                                 content='content',
                                                 name='attachment_name'))
        res.add_address(endpoint.Endpoint(url='http://192.168.0.1'))

        self.assertEqual(res.is_valid(), True)
        dict_res = res.as_dict()
        for key in resource.RESOURCE_KEYNAMES:
            self.assertIn(key, dict_res)

    def test_resource_shortform(self):
        res = resource.Resource(id='target')
        self.assertEqual(res.is_valid(), True)

        res.add_attachment(attachment.Attachment(typeURI='attachURI',
                                                 content='content',
                                                 name='attachment_name'))
        self.assertEqual(res.is_valid(), False)

    def test_event(self):
        ev = event.Event(eventType='activity',
                         id=identifier.generate_uuid(),
                         eventTime=timestamp.get_utc_now(),
                         initiator=resource.Resource(typeURI='storage'),
                         initiatorId=identifier.generate_uuid(),
                         action='read',
                         target=resource.Resource(typeURI='storage'),
                         targetId=identifier.generate_uuid(),
                         observer=resource.Resource(id='target'),
                         observerId=identifier.generate_uuid(),
                         outcome='success',
                         reason=reason.Reason(reasonType='HTTP',
                                              reasonCode='200'),
                         severity='high')
        ev.add_measurement(
            measurement.Measurement(result='100',
                                    metricId=identifier.generate_uuid())),
        ev.add_tag(tag.generate_name_value_tag('name', 'val'))
        ev.add_attachment(attachment.Attachment(typeURI='attachURI',
                                                content='content',
                                                name='attachment_name'))
        ev.observer = resource.Resource(typeURI='service/security')
        ev.add_reporterstep(reporterstep.Reporterstep(
            role='observer',
            reporter=resource.Resource(typeURI='service/security')))
        ev.add_reporterstep(reporterstep.Reporterstep(
            reporterId=identifier.generate_uuid()))
        self.assertEqual(ev.is_valid(), False)

        dict_ev = ev.as_dict()
        for key in event.EVENT_KEYNAMES:
            self.assertIn(key, dict_ev)

        ev = event.Event(eventType='activity',
                         id=identifier.generate_uuid(),
                         eventTime=timestamp.get_utc_now(),
                         initiator=resource.Resource(typeURI='storage'),
                         action='read',
                         target=resource.Resource(typeURI='storage'),
                         observer=resource.Resource(id='target'),
                         outcome='success')
        self.assertEqual(ev.is_valid(), True)

        ev = event.Event(eventType='activity',
                         id=identifier.generate_uuid(),
                         eventTime=timestamp.get_utc_now(),
                         initiatorId=identifier.generate_uuid(),
                         action='read',
                         targetId=identifier.generate_uuid(),
                         observerId=identifier.generate_uuid(),
                         outcome='success')
        self.assertEqual(ev.is_valid(), True)

        ev = event.Event(eventType='activity',
                         id=identifier.generate_uuid(),
                         eventTime=timestamp.get_utc_now(),
                         initiator=resource.Resource(typeURI='storage'),
                         action='read',
                         targetId=identifier.generate_uuid(),
                         observer=resource.Resource(id='target'),
                         outcome='success')
        self.assertEqual(ev.is_valid(), True)

    def test_event_unique(self):
        ev = event.Event(eventType='activity',
                         initiator=resource.Resource(typeURI='storage'),
                         action='read',
                         target=resource.Resource(typeURI='storage'),
                         observer=resource.Resource(id='target'),
                         outcome='success')
        time.sleep(1)
        ev2 = event.Event(eventType='activity',
                          initiator=resource.Resource(typeURI='storage'),
                          action='read',
                          target=resource.Resource(typeURI='storage'),
                          observer=resource.Resource(id='target'),
                          outcome='success')
        self.assertNotEqual(ev.id, ev2.id)
        self.assertNotEqual(ev.eventTime, ev2.eventTime)

    def test_event_resource_shortform_not_self(self):
        self.assertRaises(ValueError,
                          lambda: event.Event(
                              eventType='activity',
                              initiator=resource.Resource(typeURI='storage'),
                              action='read',
                              target=resource.Resource(id='target'),
                              observer=resource.Resource(id='target'),
                              outcome='success'))
        self.assertRaises(ValueError,
                          lambda: event.Event(
                              eventType='activity',
                              initiator=resource.Resource(id='initiator'),
                              action='read',
                              target=resource.Resource(typeURI='storage'),
                              observer=resource.Resource(id='target'),
                              outcome='success'))
