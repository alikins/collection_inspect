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

# from ansible.module_utils.basic import AnsibleModule
from ansible_collections.alikins.collection_inspect.plugins.module_utils.collection_inspect import get_dunders

log = logging.getLogger(__name__)

log_format = """%(asctime)s %(relativeCreated)d %(levelname)-0.1s %(name)s %(process)d %(funcName)s:%(lineno)d - %(message)s"""
logging.basicConfig(level=logging.DEBUG, format=log_format)

log.debug('sys.path: %s', pprint.pformat(sys.path))
log.debug('sys.meta_path: %s', pprint.pformat(sys.meta_path))

# from ansible_collections.alikins.collection_inspect.plugins.module_utils import collection_inspect
# import ansible_collections.alikins.collection_inspect.plugins.module_utils.collection_inspect


def main():

    res = {
        'success': True,
        'changed': True,
        # 'dunders': collection_inspect.get_dunders(globals(), force_serializable=True)
        # 'dunders': collection_inspect.get_dunders(globals(), force_serializable=True)
        'dunders': get_dunders(globals(), force_serializable=True)
    }
    print(json.dumps(res))
    sys.exit(0)  # pylint: disable=ansible-bad-function


if __name__ == "__main__":
    main()
