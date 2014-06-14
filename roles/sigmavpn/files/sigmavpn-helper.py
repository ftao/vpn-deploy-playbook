#!/usr/bin/env python -u
# A event listener meant to be subscribed to PROCESS_STATE_CHANGE
# events. It will reconfig the network interface when sigmavpn process is up.

# A supervisor config snippet that tells supervisor to use this script
# as a listener is below.
#
# [eventlistener:sigmavpn-helper]
# command=/usr/local/bin/sigmavpn-helper.py /usr/local/etc/sigmavpn-peers.json
# events=PROCESS_STATE
#

import os
import sys
import json
import subprocess

from supervisor import childutils

IFCONFIG_PATH = '/sbin/ifconfig'
DEFAULT_MTU = 1400

HELPER_NAME = os.environ.get('SUPERVISOR_PROCESS_NAME')

class SigmaVPNHelper(object):
    prog_name_prefix = "sigmavpn-"
    tunnel_name_pattern = "tun-sigma-%s"
    conf_path = '/usr/local/etc/sigmavpn/conf.d/'

    def __init__(self):
        self.stdin = sys.stdin
        self.stdout = sys.stdout
        self.stderr = sys.stderr


    def runforever(self, test=False):
        while 1:
            # we explicitly use self.stdin, self.stdout, and self.stderr
            # instead of sys.* so we can unit test this code
            headers, payload = childutils.listener.wait(self.stdin, self.stdout)

            if not headers['eventname'] == 'PROCESS_STATE_RUNNING':
                childutils.listener.ok(self.stdout)
                continue
            pheaders, pdata = childutils.eventdata(payload+'\n')
            processname = pheaders['processname']
            if processname != HELPER_NAME and processname.startswith(self.prog_name_prefix):
                name = processname[len(self.prog_name_prefix):]
                self.stderr.write("reconfig ip for %s" % name)
                try:
                    self.reconfig_ip(name)
                except Exception, e:
                    self.stderr.write("fail to reconfig ip %s %s" %(name, e))

            childutils.listener.ok(self.stdout)

    def reconfig_ip(self, name):
        peer = self.load_peer(name)
        subprocess.call([
            IFCONFIG_PATH, 
            self.tunnel_name_pattern % peer['name'],
            peer['virtual_ip'],
            'netmask', '255.255.255.255',
            'pointopoint', peer['peer_ip'],
            'mtu' , str(DEFAULT_MTU)
        ])
        
    def load_peer(self, name):
        path = os.path.join(self.conf_path, "%s-ip.json" %name)
        with open(path, 'r') as fp:
            return json.load(fp)

def main(argv=sys.argv):
    prog = SigmaVPNHelper()
    prog.runforever()

if __name__ == '__main__':
    main()
