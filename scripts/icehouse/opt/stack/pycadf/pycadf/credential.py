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
from pycadf import utils

TYPE_URI_CRED = cadftype.CADF_VERSION_1_0_0 + 'credential'

CRED_KEYNAME_TYPE = "type"
CRED_KEYNAME_TOKEN = "token"

CRED_KEYNAMES = [CRED_KEYNAME_TYPE,
                 CRED_KEYNAME_TOKEN]


FED_CRED_KEYNAME_IDENTITY_PROVIDER = "identity_provider"
FED_CRED_KEYNAME_USER = "user"
FED_CRED_KEYNAME_GROUPS = "groups"

FED_CRED_KEYNAMES = CRED_KEYNAMES + [FED_CRED_KEYNAME_IDENTITY_PROVIDER,
                                     FED_CRED_KEYNAME_USER,
                                     FED_CRED_KEYNAME_GROUPS]


class Credential(cadftype.CADFAbstractType):
    type = cadftype.ValidatorDescriptor(
        CRED_KEYNAME_TYPE,
        lambda x: isinstance(x, six.string_types))
    token = cadftype.ValidatorDescriptor(
        CRED_KEYNAME_TOKEN,
        lambda x: isinstance(x, six.string_types))

    def __init__(self, token, type=None):
        """Create Credential data type

        :param token: identity or security token
        :param type: type of credential (ie. identity token)
        """

        # Credential.token
        setattr(self, CRED_KEYNAME_TOKEN, utils.mask_value(token))

        # Credential.type
        if type is not None:
            setattr(self, CRED_KEYNAME_TYPE, type)

    # TODO(mrutkows): validate this cadf:Credential type against schema
    def is_valid(self):
        """Validation to ensure Credential required attributes are set."""
        # TODO(mrutkows): validate specific attribute type/format
        return self._isset(CRED_KEYNAME_TOKEN)


class FederatedCredential(Credential):
    identity_provider = cadftype.ValidatorDescriptor(
        FED_CRED_KEYNAME_IDENTITY_PROVIDER,
        lambda x: isinstance(x, six.string_types))
    user = cadftype.ValidatorDescriptor(
        FED_CRED_KEYNAME_USER,
        lambda x: isinstance(x, six.string_types))
    groups = cadftype.ValidatorDescriptor(
        FED_CRED_KEYNAME_GROUPS,
        lambda x: isinstance(x, list))

    def __init__(self, token, type, identity_provider, user, groups):
        super(FederatedCredential, self).__init__(
            token=token,
            type=type)

        # FederatedCredential.identity_provider
        setattr(self, FED_CRED_KEYNAME_IDENTITY_PROVIDER, identity_provider)

        # FederatedCredential.user
        setattr(self, FED_CRED_KEYNAME_USER, user)

        # FederatedCredential.groups
        setattr(self, FED_CRED_KEYNAME_GROUPS, groups)

    def is_valid(self):
        """Validation to ensure Credential required attributes are set."""
        return (
            super(FederatedCredential, self).is_valid()
            and self._isset(CRED_KEYNAME_TYPE)
            and self._isset(FED_CRED_KEYNAME_IDENTITY_PROVIDER)
            and self._isset(FED_CRED_KEYNAME_USER)
            and self._isset(FED_CRED_KEYNAME_GROUPS))
