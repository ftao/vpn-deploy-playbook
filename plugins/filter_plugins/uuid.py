from __future__ import absolute_import
import uuid
BASE_UUID = uuid.UUID("{FB319859-FB1F-402E-84A2-460A1FB35E4E}")

def uuid5(*args):
    def _to_str(v):
        if type(v) is unicode:
            return v.encode("utf-8")
        else:
            return str(v)
    v = ":".join(map(_to_str, args))
    return str(uuid.uuid5(BASE_UUID, v))

class FilterModule(object):
    ''' Ansible uuid jinja2 filters '''

    def filters(self):
        return {
            'uuid5': uuid5,
        }
