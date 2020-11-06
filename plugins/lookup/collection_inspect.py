from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = """
    lookup: collection_inspect
    author: Adrian Likins <alikins@redhat.com>
    version_added: "2.8"
    short_description: report info about where this plugin was loaded from
    description:
        - Inspect and introspect info about this plugin, loader, and collection
    options:
      _terms:
        description: unused list
        required: False
"""

EXAMPLES = """
- debug: msg="This plugin: Replace with real example "
"""

RETURN = """
  _raw:
    description:
      - values about the plugin and it's collection.
    type: list
"""

from ansible.plugins.lookup import LookupBase

from ansible_collections.alikins.collection_inspect.plugins.module_utils import collection_inspect


class LookupModule(LookupBase):

    def run(self, terms, variables, **kwargs):

        ret = []
        dunders = collection_inspect.get_dunders(globals())
        for key in dunders:
            ret.append((key, dunders[key]))
        return ret
