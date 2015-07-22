#!/usr/bin/env python

import json
import random
import string

def shadowsocks_generate_port_password(port_start, port_end, password_length):
	return dict(map(lambda x: (x, ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(password_length))), range(port_start, port_end)))


if __name__ == '__main__':
	print(json.dumps(shadowsocks_generate_port_password(30080, 30100, 16), indent=4, separators=(',', ':')))