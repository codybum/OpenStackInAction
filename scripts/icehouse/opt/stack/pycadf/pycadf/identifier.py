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
import six

CONF = cfg.CONF
opts = [
    cfg.StrOpt('namespace',
               default='openstack',
               help='namespace prefix for generated id'),
]
CONF.register_opts(opts, group='audit')


# TODO(mrutkows): make the namespace prefix configurable and have it resolve to
# a full openstack namespace/domain value via some declaration (e.g.
# "openstack:" == "http:\\www.openstack.org\")...
def generate_uuid():
    """Generate a CADF identifier
    """
    return norm_ns(str(uuid.uuid4()))


def norm_ns(str_id):
    """Apply a namespace to the identifier
    """
    prefix = CONF.audit.namespace + ':' if CONF.audit.namespace else ''
    return prefix + str_id


# TODO(mrutkows): validate any cadf:Identifier (type) record against
# CADF schema.  This would include schema validation as an optional parm.
def is_valid(value):
    """Validation to ensure Identifier is correct.
    """
    if not isinstance(value, six.string_types):
        raise TypeError
    return True
