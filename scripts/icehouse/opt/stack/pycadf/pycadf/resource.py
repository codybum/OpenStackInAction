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

import six

from pycadf import attachment
from pycadf import cadftaxonomy
from pycadf import cadftype
from pycadf import credential
from pycadf import endpoint
from pycadf import geolocation
from pycadf import host
from pycadf import identifier

TYPE_URI_RESOURCE = cadftype.CADF_VERSION_1_0_0 + 'resource'

RESOURCE_KEYNAME_TYPEURI = "typeURI"
RESOURCE_KEYNAME_ID = "id"
RESOURCE_KEYNAME_NAME = "name"
RESOURCE_KEYNAME_DOMAIN = "domain"
RESOURCE_KEYNAME_CRED = "credential"
RESOURCE_KEYNAME_REF = "ref"
RESOURCE_KEYNAME_GEO = "geolocation"
RESOURCE_KEYNAME_GEOID = "geolocationId"
RESOURCE_KEYNAME_HOST = "host"
RESOURCE_KEYNAME_ADDRS = "addresses"
RESOURCE_KEYNAME_ATTACHMENTS = "attachments"

RESOURCE_KEYNAMES = [RESOURCE_KEYNAME_TYPEURI,
                     RESOURCE_KEYNAME_ID,
                     RESOURCE_KEYNAME_NAME,
                     RESOURCE_KEYNAME_DOMAIN,
                     RESOURCE_KEYNAME_CRED,
                     RESOURCE_KEYNAME_REF,
                     RESOURCE_KEYNAME_GEO,
                     RESOURCE_KEYNAME_GEOID,
                     RESOURCE_KEYNAME_HOST,
                     RESOURCE_KEYNAME_ADDRS,
                     RESOURCE_KEYNAME_ATTACHMENTS]


class Resource(cadftype.CADFAbstractType):

    typeURI = cadftype.ValidatorDescriptor(
        RESOURCE_KEYNAME_TYPEURI, lambda x: cadftaxonomy.is_valid_resource(x))
    id = cadftype.ValidatorDescriptor(RESOURCE_KEYNAME_ID,
                                      lambda x: identifier.is_valid(x))
    name = cadftype.ValidatorDescriptor(RESOURCE_KEYNAME_NAME,
                                        lambda x: isinstance(x,
                                                             six.string_types))
    domain = cadftype.ValidatorDescriptor(RESOURCE_KEYNAME_DOMAIN,
                                          lambda x: isinstance(
                                              x, six.string_types))
    credential = cadftype.ValidatorDescriptor(
        RESOURCE_KEYNAME_CRED, (lambda x: isinstance(x, credential.Credential)
                                and x.is_valid()))
    host = cadftype.ValidatorDescriptor(
        RESOURCE_KEYNAME_HOST, lambda x: isinstance(x, host.Host))
    # TODO(mrutkows): validate the "ref" attribute is indeed a URI (format),
    # If it is a URL, we do not need to validate it is accessible/working,
    # for audit purposes this could have been a valid URL at some point
    # in the past or a URL that is only valid within some domain (e.g. a
    # private cloud)
    ref = cadftype.ValidatorDescriptor(RESOURCE_KEYNAME_REF,
                                       lambda x: isinstance(x,
                                                            six.string_types))
    geolocation = cadftype.ValidatorDescriptor(
        RESOURCE_KEYNAME_GEO,
        lambda x: isinstance(x, geolocation.Geolocation))
    geolocationId = cadftype.ValidatorDescriptor(
        RESOURCE_KEYNAME_GEOID, lambda x: identifier.is_valid(x))

    def __init__(self, id=None, typeURI=cadftaxonomy.UNKNOWN, name=None,
                 ref=None, domain=None, credential=None, host=None,
                 geolocation=None, geolocationId=None):
        """Resource data type

        :param id: id of resource
        :param typeURI: typeURI of resource, defaults to 'unknown' if not set
        :param name: name of resource
        :param domain: domain to qualify name of resource
        :param credential: optional security Credential data type
        :param host: optional Host data type information relating to resource
        :param geolocation: optional CADF Geolocation of resource
        :param geolocationId: optional id of CADF Geolocation for resource
        """

        # Resource.id
        setattr(self, RESOURCE_KEYNAME_ID, id or identifier.generate_uuid())

        # Resource.typeURI
        if (getattr(self, RESOURCE_KEYNAME_ID) != "target" and
                getattr(self, RESOURCE_KEYNAME_ID) != "initiator"):
            setattr(self, RESOURCE_KEYNAME_TYPEURI, typeURI)

        # Resource.name
        if name is not None:
            setattr(self, RESOURCE_KEYNAME_NAME, name)

        # Resource.ref
        if ref is not None:
            setattr(self, RESOURCE_KEYNAME_REF, ref)

        # Resource.domain
        if domain is not None:
            setattr(self, RESOURCE_KEYNAME_DOMAIN, domain)

        # Resource.credential
        if credential is not None:
            setattr(self, RESOURCE_KEYNAME_CRED, credential)

        # Resource.host
        if host is not None:
            setattr(self, RESOURCE_KEYNAME_HOST, host)

        # Resource.geolocation
        if geolocation is not None:
            setattr(self, RESOURCE_KEYNAME_GEO, geolocation)

        # Resource.geolocationId
        if geolocationId:
            setattr(self, RESOURCE_KEYNAME_GEOID, geolocationId)

    # Resource.address
    def add_address(self, addr):
        """Add CADF endpoints to Resource

        :param addr: CADF Endpoint to add to Resource
        """
        if (addr is not None and isinstance(addr, endpoint.Endpoint)):
            if addr.is_valid():
                # Create the list of Endpoints if needed
                if not hasattr(self, RESOURCE_KEYNAME_ADDRS):
                    setattr(self, RESOURCE_KEYNAME_ADDRS, list())

                addrs = getattr(self, RESOURCE_KEYNAME_ADDRS)
                addrs.append(addr)
            else:
                raise ValueError('Invalid endpoint')
        else:
            raise ValueError('Invalid endpoint. Value must be an Endpoint')

    # Resource.attachments
    def add_attachment(self, attach_val):
        """Add CADF attachment to Resource

        :param attach_val: CADF Attachment to add to Resource
        """
        if (attach_val is not None
                and isinstance(attach_val, attachment.Attachment)):
            if attach_val.is_valid():
                # Create the list of Attachments if needed
                if not hasattr(self, RESOURCE_KEYNAME_ATTACHMENTS):
                    setattr(self, RESOURCE_KEYNAME_ATTACHMENTS, list())

                attachments = getattr(self, RESOURCE_KEYNAME_ATTACHMENTS)
                attachments.append(attach_val)
            else:
                raise ValueError('Invalid attachment')
        else:
            raise ValueError('Invalid attachment. Value must be an Attachment')

    # self validate this cadf:Resource type against schema
    def is_valid(self):
        """Validation to ensure Resource required attributes are set
        """
        return (self._isset(RESOURCE_KEYNAME_ID) and
                (self._isset(RESOURCE_KEYNAME_TYPEURI) or
                 ((getattr(self, RESOURCE_KEYNAME_ID) == "target" or
                   getattr(self, RESOURCE_KEYNAME_ID) == "initiator") and
                  len(vars(self).keys()) == 1)))
        # TODO(mrutkows): validate the Resource's attribute types
