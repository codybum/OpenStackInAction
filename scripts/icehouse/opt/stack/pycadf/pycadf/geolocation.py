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

# Geolocation types can appear outside a cadf:Event record context, in these
# cases a typeURI may be used to identify the cadf:Geolocation data type.
TYPE_URI_GEOLOCATION = cadftype.CADF_VERSION_1_0_0 + 'geolocation'

GEO_KEYNAME_ID = "id"
GEO_KEYNAME_LATITUDE = "latitude"
GEO_KEYNAME_LONGITUDE = "longitude"
GEO_KEYNAME_ELEVATION = "elevation"
GEO_KEYNAME_ACCURACY = "accuracy"
GEO_KEYNAME_CITY = "city"
GEO_KEYNAME_STATE = "state"
GEO_KEYNAME_REGIONICANN = "regionICANN"
# GEO_KEYNAME_ANNOTATIONS = "annotations"

GEO_KEYNAMES = [GEO_KEYNAME_ID,
                GEO_KEYNAME_LATITUDE,
                GEO_KEYNAME_LONGITUDE,
                GEO_KEYNAME_ELEVATION,
                GEO_KEYNAME_ACCURACY,
                GEO_KEYNAME_CITY,
                GEO_KEYNAME_STATE,
                GEO_KEYNAME_REGIONICANN
                # GEO_KEYNAME_ANNOTATIONS
                ]


class Geolocation(cadftype.CADFAbstractType):

    id = cadftype.ValidatorDescriptor(GEO_KEYNAME_ID,
                                      lambda x: identifier.is_valid(x))
    # TODO(mrutkows): we may want to do more validation to make
    # sure numeric range represented by string is valid
    latitude = cadftype.ValidatorDescriptor(GEO_KEYNAME_LATITUDE,
                                            lambda x: isinstance(
                                                x, six.string_types))
    longitude = cadftype.ValidatorDescriptor(GEO_KEYNAME_LONGITUDE,
                                             lambda x: isinstance(
                                                 x, six.string_types))
    elevation = cadftype.ValidatorDescriptor(GEO_KEYNAME_ELEVATION,
                                             lambda x: isinstance(
                                                 x, six.string_types))
    accuracy = cadftype.ValidatorDescriptor(GEO_KEYNAME_ACCURACY,
                                            lambda x: isinstance(
                                                x, six.string_types))
    city = cadftype.ValidatorDescriptor(GEO_KEYNAME_CITY,
                                        lambda x: isinstance(
                                            x, six.string_types))
    state = cadftype.ValidatorDescriptor(GEO_KEYNAME_STATE,
                                         lambda x: isinstance(
                                             x, six.string_types))
    regionICANN = cadftype.ValidatorDescriptor(
        GEO_KEYNAME_REGIONICANN,
        lambda x: isinstance(x, six.string_types))

    def __init__(self, id=None, latitude=None, longitude=None,
                 elevation=None, accuracy=None, city=None, state=None,
                 regionICANN=None):
        """Create Geolocation data type

        :param id: id of geolocation
        :param latitude: latitude of geolocation
        :param longitude: longitude of geolocation
        :param elevation: elevation of geolocation in meters
        :param accuracy: accuracy of geolocation in meters
        :param city: city of geolocation
        :param state: state/province of geolocation
        :param regionICANN: region of geolocation (ie. country)
        """

        # Geolocation.id
        if id is not None:
            setattr(self, GEO_KEYNAME_ID, id)

        # Geolocation.latitude
        if latitude is not None:
            setattr(self, GEO_KEYNAME_LATITUDE, latitude)

        # Geolocation.longitude
        if longitude is not None:
            setattr(self, GEO_KEYNAME_LONGITUDE, longitude)

        # Geolocation.elevation
        if elevation is not None:
            setattr(self, GEO_KEYNAME_ELEVATION, elevation)

        # Geolocation.accuracy
        if accuracy is not None:
            setattr(self, GEO_KEYNAME_ACCURACY, accuracy)

        # Geolocation.city
        if city is not None:
            setattr(self, GEO_KEYNAME_CITY, city)

        # Geolocation.state
        if state is not None:
            setattr(self, GEO_KEYNAME_STATE, state)

        # Geolocation.regionICANN
        if regionICANN is not None:
            setattr(self, GEO_KEYNAME_REGIONICANN, regionICANN)

    # TODO(mrutkows): add mechanism for annotations, OpenStack may choose
    # not to support this "extension mechanism" and is not required (and not
    # critical in many audit contexts)
    def set_annotations(self, value):
        raise NotImplementedError()
        # setattr(self, GEO_KEYNAME_ANNOTATIONS, value)

    # self validate cadf:Geolocation type
    def is_valid(self):
        return True
