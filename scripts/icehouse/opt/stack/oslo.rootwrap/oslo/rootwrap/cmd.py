# Copyright (c) 2011 OpenStack Foundation.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""Root wrapper for OpenStack services

   Filters which commands a service is allowed to run as another user.

   To use this with oslo, you should set the following in
   oslo.conf:
   rootwrap_config=/etc/oslo/rootwrap.conf

   You also need to let the oslo user run oslo-rootwrap
   as root in sudoers:
   oslo ALL = (root) NOPASSWD: /usr/bin/oslo-rootwrap
                                   /etc/oslo/rootwrap.conf *

   Service packaging should deploy .filters files only on nodes where
   they are needed, to avoid allowing more than is necessary.
"""

from __future__ import print_function

import logging
import sys

from six import moves

from oslo.rootwrap import daemon as daemon_mod
from oslo.rootwrap import wrapper

RC_UNAUTHORIZED = 99
RC_NOCOMMAND = 98
RC_BADCONFIG = 97
RC_NOEXECFOUND = 96


def _exit_error(execname, message, errorcode, log=True):
    print("%s: %s" % (execname, message), file=sys.stderr)
    if log:
        logging.error(message)
    sys.exit(errorcode)


def daemon():
    return main(run_daemon=True)


def main(run_daemon=False):
    # Split arguments, require at least a command
    execname = sys.argv.pop(0)
    if run_daemon:
        if len(sys.argv) != 1:
            _exit_error(execname, "Extra arguments to daemon", RC_NOCOMMAND,
                        log=False)
    else:
        if len(sys.argv) < 2:
            _exit_error(execname, "No command specified", RC_NOCOMMAND,
                        log=False)

    configfile = sys.argv.pop(0)

    # Load configuration
    try:
        rawconfig = moves.configparser.RawConfigParser()
        rawconfig.read(configfile)
        config = wrapper.RootwrapConfig(rawconfig)
    except ValueError as exc:
        msg = "Incorrect value in %s: %s" % (configfile, exc.message)
        _exit_error(execname, msg, RC_BADCONFIG, log=False)
    except moves.configparser.Error:
        _exit_error(execname, "Incorrect configuration file: %s" % configfile,
                    RC_BADCONFIG, log=False)

    if config.use_syslog:
        wrapper.setup_syslog(execname,
                             config.syslog_log_facility,
                             config.syslog_log_level)

    filters = wrapper.load_filters(config.filters_path)

    if run_daemon:
        daemon_mod.daemon_start(config, filters)
    else:
        run_one_command(execname, config, filters, sys.argv)


def run_one_command(execname, config, filters, userargs):
    # Execute command if it matches any of the loaded filters
    try:
        obj = wrapper.start_subprocess(
            filters, userargs,
            exec_dirs=config.exec_dirs,
            log=config.use_syslog,
            stdin=sys.stdin,
            stdout=sys.stdout,
            stderr=sys.stderr)
        obj.wait()
        sys.exit(obj.returncode)

    except wrapper.FilterMatchNotExecutable as exc:
        msg = ("Executable not found: %s (filter match = %s)"
               % (exc.match.exec_path, exc.match.name))
        _exit_error(execname, msg, RC_NOEXECFOUND, log=config.use_syslog)

    except wrapper.NoFilterMatched:
        msg = ("Unauthorized command: %s (no filter matched)"
               % ' '.join(userargs))
        _exit_error(execname, msg, RC_UNAUTHORIZED, log=config.use_syslog)
