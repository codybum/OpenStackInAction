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
from pycadf import metric
from pycadf import resource

MEASUREMENT_KEYNAME_RESULT = "result"
MEASUREMENT_KEYNAME_METRIC = "metric"
MEASUREMENT_KEYNAME_METRICID = "metricId"
MEASUREMENT_KEYNAME_CALCBY = "calculatedBy"

MEASUREMENT_KEYNAMES = [MEASUREMENT_KEYNAME_RESULT,
                        MEASUREMENT_KEYNAME_METRICID,
                        MEASUREMENT_KEYNAME_METRIC,
                        MEASUREMENT_KEYNAME_CALCBY]


class Measurement(cadftype.CADFAbstractType):

    result = cadftype.ValidatorDescriptor(MEASUREMENT_KEYNAME_RESULT)
    metric = cadftype.ValidatorDescriptor(
        MEASUREMENT_KEYNAME_METRIC, lambda x: isinstance(x, metric.Metric))
    metricId = cadftype.ValidatorDescriptor(MEASUREMENT_KEYNAME_METRICID,
                                            lambda x: identifier.is_valid(x))
    calculatedBy = cadftype.ValidatorDescriptor(
        MEASUREMENT_KEYNAME_CALCBY,
        (lambda x: isinstance(x, resource.Resource) and x.is_valid()))

    def __init__(self, result=None, metric=None, metricId=None,
                 calculatedBy=None):
        """Create Measurement data type

        :param result: value of measurement
        :param metric: Metric data type of current measurement
        :param metricId: id of Metric data type of current measurement
        :param calculatedBy: Resource that calculated measurement
        """
        # Measurement.result
        if result is not None:
            setattr(self, MEASUREMENT_KEYNAME_RESULT, result)

        # Measurement.metricId
        if metricId is not None:
            setattr(self, MEASUREMENT_KEYNAME_METRICID, metricId)

        # Measurement.metric
        if metric is not None:
            setattr(self, MEASUREMENT_KEYNAME_METRIC, metric)

        # Measurement.calculaedBy
        if calculatedBy is not None:
            setattr(self, MEASUREMENT_KEYNAME_CALCBY, calculatedBy)

    # self validate this cadf:Measurement type against schema
    def is_valid(self):
        """Validation to ensure Measurement required attributes are set.
        """
        return (self._isset(MEASUREMENT_KEYNAME_RESULT) and
                (self._isset(MEASUREMENT_KEYNAME_METRIC) ^
                 self._isset(MEASUREMENT_KEYNAME_METRICID)))
