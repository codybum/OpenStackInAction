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

from pycadf import cadftype
from pycadf import identifier
from pycadf import resource
from pycadf import timestamp

REPORTERSTEP_KEYNAME_ROLE = "role"
REPORTERSTEP_KEYNAME_REPORTER = "reporter"
REPORTERSTEP_KEYNAME_REPORTERID = "reporterId"
REPORTERSTEP_KEYNAME_REPORTERTIME = "reporterTime"
# REPORTERSTEP_KEYNAME_ATTACHMENTS = "attachments"

REPORTERSTEP_KEYNAMES = [REPORTERSTEP_KEYNAME_ROLE,
                         REPORTERSTEP_KEYNAME_REPORTER,
                         REPORTERSTEP_KEYNAME_REPORTERID,
                         REPORTERSTEP_KEYNAME_REPORTERTIME,
                         # REPORTERSTEP_KEYNAME_ATTACHMENTS
                         ]


class Reporterstep(cadftype.CADFAbstractType):

    role = cadftype.ValidatorDescriptor(
        REPORTERSTEP_KEYNAME_ROLE,
        lambda x: cadftype.is_valid_reporter_role(x))
    reporter = cadftype.ValidatorDescriptor(
        REPORTERSTEP_KEYNAME_REPORTER,
        (lambda x: isinstance(x, resource.Resource) and x.is_valid()))
    reporterId = cadftype.ValidatorDescriptor(
        REPORTERSTEP_KEYNAME_REPORTERID, lambda x: identifier.is_valid(x))
    reporterTime = cadftype.ValidatorDescriptor(
        REPORTERSTEP_KEYNAME_REPORTERTIME, lambda x: timestamp.is_valid(x))

    def __init__(self, role=cadftype.REPORTER_ROLE_MODIFIER,
                 reporterTime=None, reporter=None, reporterId=None):
        """Create ReporterStep data type

        :param role: optional role of Reporterstep. Defaults to 'modifier'
        :param reporterTime: utc time of Reporterstep.
        :param reporter: CADF Resource of reporter
        :param reporterId: id of CADF resource for reporter
        """
        # Reporterstep.role
        setattr(self, REPORTERSTEP_KEYNAME_ROLE, role)

        # Reporterstep.reportTime
        if reporterTime is not None:
            setattr(self, REPORTERSTEP_KEYNAME_REPORTERTIME, reporterTime)

        # Reporterstep.reporter
        if reporter is not None:
            setattr(self, REPORTERSTEP_KEYNAME_REPORTER, reporter)

        # Reporterstep.reporterId
        if reporterId is not None:
            setattr(self, REPORTERSTEP_KEYNAME_REPORTERID, reporterId)

    # self validate this cadf:Reporterstep type against schema
    def is_valid(self):
        """Validation to ensure Reporterstep required attributes are set.
        """
        return (
            self._isset(REPORTERSTEP_KEYNAME_ROLE) and
            (self._isset(REPORTERSTEP_KEYNAME_REPORTER) ^
             self._isset(REPORTERSTEP_KEYNAME_REPORTERID))
        )
