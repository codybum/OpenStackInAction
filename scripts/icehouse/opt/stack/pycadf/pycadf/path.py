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


class Path(cadftype.CADFAbstractType):

    def set_path_absolute(self):
        # TODO(mrutkows): validate absolute path format, else Type error
        raise NotImplementedError()

    def set_path_relative(self):
        # TODO(mrutkows); validate relative path format, else Type error
        raise NotImplementedError()

    # TODO(mrutkows): validate any cadf:Path (type) record against CADF schema
    @staticmethod
    def is_valid(value):
        if not isinstance(value, six.string_types):
            raise TypeError

        return True
