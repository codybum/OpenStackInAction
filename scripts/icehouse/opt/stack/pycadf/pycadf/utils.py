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


def mask_value(value, s_percent=0.125):
    """Obfuscate a given string to show only a percentage of leading
    and trailing characters.

    :param s_percent: The percentage (in decimal) of characters to replace
    """
    if isinstance(value, six.string_types):
        visible = (32 if int(round(len(value) * s_percent)) > 32
                   else int(round(len(value) * s_percent)))
        return value[:visible] + " xxxxxxxx " + value[-visible:]
    return value
