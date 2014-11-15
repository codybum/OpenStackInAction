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

import datetime

import pytz
import six

TIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%f%z"


def get_utc_now(timezone=None):
    """Return the current UTC time.

    :param timezone: an optional timezone param to offset time to.
    """
    utc_datetime = pytz.utc.localize(datetime.datetime.utcnow())
    if timezone is not None:
        try:
            utc_datetime = utc_datetime.astimezone(pytz.timezone(timezone))
        except Exception:
            utc_datetime.strftime(TIME_FORMAT)
    return utc_datetime.strftime(TIME_FORMAT)


# TODO(mrutkows): validate any cadf:Timestamp (type) record against
# CADF schema
def is_valid(value):
    """Validation to ensure timestamp is a string.
    """
    if not isinstance(value, six.string_types):
        raise ValueError('Timestamp should be a String')

    return True
