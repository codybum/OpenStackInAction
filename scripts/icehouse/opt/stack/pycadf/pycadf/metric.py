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
from pycadf import identifier

# Metric types can appear outside a cadf:Event record context, in these cases
# a typeURI may be used to identify the cadf:Metric data type.
TYPE_URI_METRIC = cadftype.CADF_VERSION_1_0_0 + 'metric'

METRIC_KEYNAME_METRICID = "metricId"
METRIC_KEYNAME_UNIT = "unit"
METRIC_KEYNAME_NAME = "name"
# METRIC_KEYNAME_ANNOTATIONS = "annotations"

METRIC_KEYNAMES = [METRIC_KEYNAME_METRICID,
                   METRIC_KEYNAME_UNIT,
                   METRIC_KEYNAME_NAME
                   # METRIC_KEYNAME_ANNOTATIONS
                   ]


class Metric(cadftype.CADFAbstractType):

    metricId = cadftype.ValidatorDescriptor(METRIC_KEYNAME_METRICID,
                                            lambda x: identifier.is_valid(x))
    unit = cadftype.ValidatorDescriptor(METRIC_KEYNAME_UNIT,
                                        lambda x: isinstance(x,
                                                             six.string_types))
    name = cadftype.ValidatorDescriptor(METRIC_KEYNAME_NAME,
                                        lambda x: isinstance(x,
                                                             six.string_types))

    def __init__(self, metricId=None, unit=None, name=None):
        """Create metric data type

        :param metricId: id of metric. uuid generated if not provided
        :param unit: unit of metric
        :param name: name of metric
        """
        # Metric.id
        setattr(self, METRIC_KEYNAME_METRICID,
                metricId or identifier.generate_uuid())

        # Metric.unit
        if unit is not None:
            setattr(self, METRIC_KEYNAME_UNIT, unit)

        # Metric.name
        if name is not None:
            setattr(self, METRIC_KEYNAME_NAME, name)

    # TODO(mrutkows): add mechanism for annotations, OpenStack may choose
    # not to support this "extension mechanism" and is not required (and not
    # critical in many audit contexts)
    def set_annotations(self, value):
        raise NotImplementedError()
        # setattr(self, METRIC_KEYNAME_ANNOTATIONS, value)

    # self validate cadf:Metric type against schema
    def is_valid(self):
        """Validation to ensure Metric required attributes are set.
        """
        # Existence test, id, and unit attributes must both exist
        return (
            self._isset(METRIC_KEYNAME_METRICID) and
            self._isset(METRIC_KEYNAME_UNIT)
        )
