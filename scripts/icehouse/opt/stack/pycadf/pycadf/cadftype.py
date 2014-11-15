# Copyright (c) 2013 IBM Corporation
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

import abc

import six

from pycadf.openstack.common import jsonutils

CADF_SCHEMA_1_0_0 = 'cadf:'
CADF_VERSION_1_0_0 = 'http://schemas.dmtf.org/cloud/audit/1.0/'

# Valid cadf:Event record "types"
EVENTTYPE_ACTIVITY = 'activity'
EVENTTYPE_MONITOR = 'monitor'
EVENTTYPE_CONTROL = 'control'

VALID_EVENTTYPES = frozenset([
    EVENTTYPE_ACTIVITY,
    EVENTTYPE_MONITOR,
    EVENTTYPE_CONTROL
])


def is_valid_eventType(value):
    return value in VALID_EVENTTYPES

# valid cadf:Event record "Reporter" roles
REPORTER_ROLE_OBSERVER = 'observer'
REPORTER_ROLE_MODIFIER = 'modifier'
REPORTER_ROLE_RELAY = 'relay'

VALID_REPORTER_ROLES = frozenset([
    REPORTER_ROLE_OBSERVER,
    REPORTER_ROLE_MODIFIER,
    REPORTER_ROLE_RELAY
])


def is_valid_reporter_role(value):
    return value in VALID_REPORTER_ROLES


class ValidatorDescriptor(object):
    def __init__(self, name, func=None):
        self.name = name
        self.func = func

    def __set__(self, instance, value):
        if value is not None:
            if self.func is not None:
                if self.func(value):
                    instance.__dict__[self.name] = value
                else:
                    raise ValueError('%s failed validation: %s' %
                                     (self.name, self.func))
            else:
                instance.__dict__[self.name] = value
        else:
            raise ValueError('%s must not be None.' % self.name)


class CADFAbstractType(six.with_metaclass(abc.ABCMeta, object)):
    """The abstract base class for all CADF (complex) data types (classes)."""

    @abc.abstractmethod
    def is_valid(self, value):
        pass

    def as_dict(self):
        """Return dict representation of Event."""
        return jsonutils.to_primitive(self, convert_instances=True)

    def _isset(self, attr):
        """Check to see if attribute is defined."""
        try:
            if isinstance(getattr(self, attr), ValidatorDescriptor):
                return False
            return True
        except AttributeError:
            return False

    # TODO(mrutkows): Eventually, we want to use the OrderedDict (introduced
    # in Python 2.7) type for all CADF classes to store attributes in a
    # canonical form.  Currently, OpenStack/Jenkins requires 2.6 compatibility
    # The reason is that we want to be able to support signing all or parts
    # of the event record and need to guarantee order.
    # def to_ordered_dict(self, value):
    #    pass
