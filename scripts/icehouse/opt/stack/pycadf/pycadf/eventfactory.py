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
from pycadf import event

ERROR_UNKNOWN_EVENTTYPE = 'Unknown CADF EventType requested on factory method'


class EventFactory(object):
    """Factory class to create different required attributes for
       the following CADF event types:
       'activity': for tracking any interesting system activities for audit
       'monitor': Events that carry Metrics and Measurements and support
       standards such as NIST
       'control': For audit events that are based upon (security) policies
       and reflect some policy decision.
    """
    def new_event(self, eventType=cadftype.EVENTTYPE_ACTIVITY, **kwargs):
        """Create new event

        :param eventType: eventType of event. Defaults to 'activity'
        """

        # for now, construct a base ('activity') event as the default
        event_val = event.Event(**kwargs)

        if not cadftype.is_valid_eventType(eventType):
            raise ValueError(ERROR_UNKNOWN_EVENTTYPE)

        event_val.eventType = eventType

        # TODO(mrutkows): CADF is only being used for basic
        # 'activity' auditing (on APIs), An IF-ELIF will
        # become more meaningful as we add support for other
        # event types.
        # elif eventType == cadftype.EVENTTYPE_MONITOR:
        #    # TODO(mrutkows): If we add support for standard (NIST)
        #    # monitoring messages, we will would have a "monitor"
        #    # subclass of the CADF Event type and create it here
        #    event_val.set_eventType(cadftype.EVENTTYPE_MONITOR)
        # elif eventType == cadftype.EVENTTYPE_CONTROL:
        #    # TODO(mrutkows): If we add support for standard (NIST)
        #    # monitoring messages, we will would have a "control"
        #    # subclass of the CADF Event type and create it here
        #    event_val.set_eventType(cadftype.EVENTTYPE_CONTROL)
        return event_val
