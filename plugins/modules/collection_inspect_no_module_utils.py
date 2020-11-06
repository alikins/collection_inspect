#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

import json
import sys
import logging
import pprint
log = logging.getLogger(__name__)

log_format = """%(asctime)s %(relativeCreated)d %(levelname)-0.1s %(name)s %(process)d %(funcName)s:%(lineno)d - %(message)s"""
logging.basicConfig(level=logging.DEBUG, format=log_format)

log.debug('sys.path: %s', pprint.pformat(sys.path))
log.debug('sys.meta_path: %s', pprint.pformat(sys.meta_path))


# This is a dupe of get_collection_inspect, except with get_dunders inlined so there is
# no attempted import of module_utils

def get_dunders(_globals, force_serializable=True):
    '''Pass in the dict returned from globals() from caller

    ie, call like:

        dunders = get_dunders(globals())

    Plugin types that runs in a worker or otherwise need to serialize
    the results to JSON should use force_serializable=True. For
    example, a module needs to use force_serializable=True.
    '''

    dunder_candidates = ('__cached__', '__file__', '__loader__',
                         '__name__', '__package__', '__path__', '__spec__')

    not_defined_blurb = '_IS_NOT_DEFINED'

    data = {}
    for candidate in dunder_candidates:
        value = _globals.get(candidate,
                             "%s%s" % (candidate.upper(), not_defined_blurb))
        if force_serializable:
            data[candidate] = "%r" % value
        else:
            data[candidate] = value

    return data


def main():

    res = {
        'success': True,
        'changed': True,
        # 'dunders': collection_inspect.get_dunders(globals(), force_serializable=True)
        'dunders': get_dunders(globals(), force_serializable=True)
    }
    print(json.dumps(res))
    sys.exit(0)  # pylint: disable=ansible-bad-function


if __name__ == "__main__":
    main()
