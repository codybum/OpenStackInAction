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

import uuid

from pycadf.tests import base
from pycadf import utils


class TestUtils(base.TestCase):
    def test_mask_value(self):
        value = str(uuid.uuid4())
        m_percent = 0.125
        obfuscate = utils.mask_value(value, m_percent)
        visible = int(round(len(value) * m_percent))
        self.assertEqual(value[:visible], obfuscate[:visible])
        self.assertNotEqual(value[:visible + 1], obfuscate[:visible + 1])
        self.assertEqual(value[-visible:], obfuscate[-visible:])
        self.assertNotEqual(value[-visible - 1:], obfuscate[-visible - 1:])
