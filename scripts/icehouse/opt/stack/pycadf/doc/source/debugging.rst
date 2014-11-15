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

.. _debugging:

===================
 Debugging with PDB
===================

Using PDB breakpoints with tox and testr normally doesn't work since the tests
just fail with a BdbQuit exception rather than stopping at the breakpoint.

To run with PDB breakpoints during testing, use the ``debug`` tox environment
rather than ``py27``. Here's an example, passing the name of a test since
you'll normally only want to run the test that hits your breakpoint::

    $ tox -e debug pycadf.tests.test_cadf_spec

For reference, the ``debug`` tox environment implements the instructions
here: https://wiki.openstack.org/wiki/Testr#Debugging_.28pdb.29_Tests
The pyCADF library provides a tox environment that enables pdb based
debugging of test cases.

