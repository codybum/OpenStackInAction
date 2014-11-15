# Copyright (c) 2014 Mirantis Inc.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import os

if os.environ.get('TEST_EVENTLET', False):
    import eventlet
    eventlet.monkey_patch()

    from tests import test_functional

    class RootwrapDaemonTest(test_functional.RootwrapDaemonTest):
        def assert_unpatched(self):
            # This test case is specifically for eventlet testing
            pass

        def test_graceful_death(self):
            # This test fails with eventlet on Python 2.6.6 on CentOS
            self.skip("Eventlet doesn't like FIFOs")
