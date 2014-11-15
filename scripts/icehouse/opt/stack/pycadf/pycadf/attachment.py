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

from pycadf import cadftype

ATTACHMENT_KEYNAME_TYPEURI = "typeURI"
ATTACHMENT_KEYNAME_CONTENT = "content"
ATTACHMENT_KEYNAME_NAME = "name"

ATTACHMENT_KEYNAMES = [ATTACHMENT_KEYNAME_TYPEURI,
                       ATTACHMENT_KEYNAME_CONTENT,
                       ATTACHMENT_KEYNAME_NAME]


class Attachment(cadftype.CADFAbstractType):

    # TODO(mrutkows): OpenStack / Ceilometer may want to define
    # the set of approved attachment types in order to
    # limit and validate them.
    typeURI = cadftype.ValidatorDescriptor(ATTACHMENT_KEYNAME_TYPEURI,
                                           lambda x: isinstance(
                                               x, six.string_types))
    content = cadftype.ValidatorDescriptor(ATTACHMENT_KEYNAME_CONTENT)
    name = cadftype.ValidatorDescriptor(ATTACHMENT_KEYNAME_NAME,
                                        lambda x: isinstance(x,
                                                             six.string_types))

    def __init__(self, typeURI=None, content=None, name=None):
        """Create Attachment data type

        :param typeURI: uri that identifies type of data in content
        :param content: container that contains any type of data
        :param contentType: name used to identify content.
        """
        # Attachment.typeURI
        if typeURI is not None:
            setattr(self, ATTACHMENT_KEYNAME_TYPEURI, typeURI)

        # Attachment.content
        if content is not None:
            setattr(self, ATTACHMENT_KEYNAME_CONTENT, content)

        # Attachment.name
        if name is not None:
            setattr(self, ATTACHMENT_KEYNAME_NAME, name)

    # self validate cadf:Attachment type against schema
    def is_valid(self):
        """Validation to ensure Attachment required attributes are set.
        """
        return (
            self._isset(ATTACHMENT_KEYNAME_TYPEURI) and
            self._isset(ATTACHMENT_KEYNAME_NAME) and
            self._isset(ATTACHMENT_KEYNAME_CONTENT)
        )
