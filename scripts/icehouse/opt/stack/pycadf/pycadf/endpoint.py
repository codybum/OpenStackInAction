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

import six

from pycadf import cadftype

TYPE_URI_ENDPOINT = cadftype.CADF_VERSION_1_0_0 + 'endpoint'

ENDPOINT_KEYNAME_URL = "url"
ENDPOINT_KEYNAME_NAME = "name"
ENDPOINT_KEYNAME_PORT = "port"

ENDPOINT_KEYNAMES = [ENDPOINT_KEYNAME_URL,
                     ENDPOINT_KEYNAME_NAME,
                     ENDPOINT_KEYNAME_PORT]


class Endpoint(cadftype.CADFAbstractType):

    url = cadftype.ValidatorDescriptor(
        ENDPOINT_KEYNAME_URL, lambda x: isinstance(x, six.string_types))
    name = cadftype.ValidatorDescriptor(
        ENDPOINT_KEYNAME_NAME, lambda x: isinstance(x, six.string_types))
    port = cadftype.ValidatorDescriptor(
        ENDPOINT_KEYNAME_PORT, lambda x: isinstance(x, six.string_types))

    def __init__(self, url, name=None, port=None):
        """Create Endpoint data type

        :param url: address of endpoint
        :param name: name of endpoint
        :param port: port of endpoint
        """

        # ENDPOINT.url
        setattr(self, ENDPOINT_KEYNAME_URL, url)
        # ENDPOINT.name
        if name is not None:
            setattr(self, ENDPOINT_KEYNAME_NAME, name)
        # ENDPOINT.port
        if port is not None:
            setattr(self, ENDPOINT_KEYNAME_PORT, port)

    # TODO(mrutkows): validate this cadf:ENDPOINT type against schema
    def is_valid(self):
        """Validation to ensure Endpoint required attributes are set.
        """
        return self._isset(ENDPOINT_KEYNAME_URL)
