# (c) 2012, Daniel Hokka Zakrisson <daniel@hozac.com>
# (c) 2013, Javier Candeira <javier@candeira.com>
# (c) 2013, Maykel Moya <mmoya@speedyrails.com>
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.

# This is openvpn static key lookup plugin based on ansible builtin password lookup
# (c) 2015, Tao Fei <filia.tao@gmail.com>

from __future__ import (absolute_import, division, print_function)

import os
import errno
import string
import random
from ansible import utils, errors
try:
    from ansible.utils.path import makedirs_safe
except:
    def makedirs_safe(path, mode=None):
        '''Safe way to create dirs in muliprocess/thread environments'''
        if not os.path.exists(path):
            try:
                if mode:
                    os.makedirs(path, mode)
                else:
                    os.makedirs(path)
            except OSError, e:
                if e.errno != errno.EEXIST:
                    raise

OPENVPN_STATIC_KEY_HEAD = '-----BEGIN OpenVPN Static key V1-----\n'
OPENVPN_STATIC_KEY_TAIL = '-----END OpenVPN Static key V1-----\n'

class LookupModule(object):

    def __init__(self, length=None, encrypt=None, basedir=None, **kwargs):
        self.basedir = basedir

    def run(self, terms, inject=None, **kwargs):

        terms = utils.listify_lookup_plugin_terms(terms, self.basedir, inject) 
        ret = []

        for term in terms:
            # you can't have escaped spaces in yor pathname
            params = term.split()
            relpath = params[0]
            # get password or create it if file doesn't exist
            path = utils.path_dwim(self.basedir, relpath)
            if not os.path.exists(path):
                pathdir = os.path.dirname(path)
                try:
                    makedirs_safe(pathdir, mode=0o700)
                except OSError as e:
                    raise errors.AnsibleError("cannot create the path for the openvpn static key lookup: %s (error was %s)" % (pathdir, str(e)))

                chars = string.hexdigits
                length = 256
                content = ''.join(random.choice(chars) for _ in range(length))
                with open(path, 'w') as f:
                    os.chmod(path, 0o600)
                    f.write(OPENVPN_STATIC_KEY_HEAD)
                    for i in range(256//32):
                        f.write(content[i*32:(i+1)*32] + '\n')
                    f.write(OPENVPN_STATIC_KEY_TAIL)
            else:
                content = open(path).read().rstrip()

            ret.append(content)

        return ret

