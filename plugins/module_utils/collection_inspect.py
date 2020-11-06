from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


def get_dunders(_globals, force_serializable=True):
    '''Pass in the dict returned from globals() from caller

    ie, call like:

        dunders = get_dunders(globals())

    Plugin types that runs in a worker or otherwise need to serialize
    the results to JSON should use force_serializable=True. For
    example, a module needs to use force_serializable=True.
    '''

    dunder_candidates = ('__cached__', '__file__', '__loader__',
                         '__name__', '__package__', '__path__', '__spec__',
                         'collection', 'collection_type',
                         '__collection__', '__collection_type__')

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
