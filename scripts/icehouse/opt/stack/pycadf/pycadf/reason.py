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

TYPE_URI_REASON = cadftype.CADF_VERSION_1_0_0 + 'reason'

REASON_KEYNAME_REASONTYPE = "reasonType"
REASON_KEYNAME_REASONCODE = "reasonCode"
REASON_KEYNAME_POLICYTYPE = "policyType"
REASON_KEYNAME_POLICYID = "policyId"

REASON_KEYNAMES = [REASON_KEYNAME_REASONTYPE,
                   REASON_KEYNAME_REASONCODE,
                   REASON_KEYNAME_POLICYTYPE,
                   REASON_KEYNAME_POLICYID]


class Reason(cadftype.CADFAbstractType):

    reasonType = cadftype.ValidatorDescriptor(
        REASON_KEYNAME_REASONTYPE,
        lambda x: isinstance(x, six.string_types))
    reasonCode = cadftype.ValidatorDescriptor(
        REASON_KEYNAME_REASONCODE,
        lambda x: isinstance(x, six.string_types))
    policyType = cadftype.ValidatorDescriptor(
        REASON_KEYNAME_POLICYTYPE,
        lambda x: isinstance(x, six.string_types))
    policyId = cadftype.ValidatorDescriptor(
        REASON_KEYNAME_POLICYID,
        lambda x: isinstance(x, six.string_types))

    def __init__(self, reasonType=None, reasonCode=None, policyType=None,
                 policyId=None):
        """Create Reason data type

        :param reasonType: domain URI which describes reasonCode
        :param reasonCode: detailed result code
        :param policyType: domain URI which describes policyId
        :param policyId: id of policy applied that describes outcome
        """

        # Reason.reasonType
        if reasonType is not None:
            setattr(self, REASON_KEYNAME_REASONTYPE, reasonType)

        # Reason.reasonCode
        if reasonCode is not None:
            setattr(self, REASON_KEYNAME_REASONCODE, reasonCode)

        # Reason.policyType
        if policyType is not None:
            setattr(self, REASON_KEYNAME_POLICYTYPE, policyType)

        # Reason.policyId
        if policyId is not None:
            setattr(self, REASON_KEYNAME_POLICYID, policyId)

    # TODO(mrutkows): validate this cadf:Reason type against schema
    def is_valid(self):
        """Validation to ensure Reason required attributes are set.
        """
        # MUST have at least one valid pairing of reason+code or policy+id
        return ((self._isset(REASON_KEYNAME_REASONTYPE) and
                 self._isset(REASON_KEYNAME_REASONCODE)) or
                (self._isset(REASON_KEYNAME_POLICYTYPE) and
                 self._isset(REASON_KEYNAME_POLICYID)))
