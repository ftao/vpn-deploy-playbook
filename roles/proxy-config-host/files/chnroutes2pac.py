#!/usr/bin/env python
from argparse import ArgumentParser
import textwrap
from chnroutes import  parse_ip_data, fetch_ip_data


intranet = [
    ["127.0.0.0", "255.0.0.0"],
    ["10.0.0.0", "255.0.0.0"],
    ["172.16.0.0", "255.0.0.0"],
    ["192.168.0.0", "255.255.0.0"],
]

def generate_pac(ip_data, path, proxy):
    proxy_pac = open(path, "wb")

    proxy_pac.write('PROXY = "%s";\n' % proxy)

    proxy_pac.write('INTRANET = [\n')
    for ip, mask in intranet:
        proxy_pac.write('    ["%s", "%s"],\n' % (ip, mask))
    proxy_pac.write("];\n\n")


    proxy_pac.write('CHINESE_SUBNETS = [\n')
    for ip, mask, _ in ip_data:
        proxy_pac.write('    ["%s", "%s"],\n' % (ip, mask))
    proxy_pac.write("];\n\n")

    logic = textwrap.dedent("""\
    function isIntranet(ip) {
        for (var i = 0; i < INTRANET.length; i++) {
            var subnet = INTRANET[i][0];
            var netmask = INTRANET[i][1];
            if (isInNet(ip, subnet, netmask)) {
                return true;
            }
        }
        return false;
    };
 
    function inChina(ip)
    {
        for (var i = 0; i < CHINESE_SUBNETS.length; i++) {
            var subnet = CHINESE_SUBNETS[i][0];
            var netmask = CHINESE_SUBNETS[i][1];
            if (isInNet(ip, subnet, netmask)) {
                return true;
            }
        }
        return false;
    }

    function FindProxyForURL(url, host)
    {
        var ip = dnsResolve(host);
        if (isIntranet(ip) || inChina(ip)) {
            return "DIRECT";
        }
        else {
            return PROXY;
        }
    }
    """)

    proxy_pac.write(logic)
    proxy_pac.close()

def parse_args():
    parser = ArgumentParser()
    parser.add_argument('-i', '--input', dest='input', 
                          help='path to apnic data file', metavar='APNICDATA')
    parser.add_argument('-f', '--file', dest='output', required=True,
                      help='path to output pac', metavar='PAC')
    parser.add_argument('-p', '--proxy', dest='proxy', required=True,
                        help='the proxy parameter in the pac file, for example,\
                        "SOCKS5 127.0.0.1:1080;"', metavar='PROXY')
    return parser.parse_args()

def main():
    args = parse_args()
    if args.input:
       with open(args.input, 'r') as fp:
            ip_data = parse_ip_data(fp.read())
    else:
        ip_data = fetch_ip_data()
    generate_pac(ip_data, args.output, args.proxy)
    print 'generate pac done'

if __name__ == "__main__":
    main()
