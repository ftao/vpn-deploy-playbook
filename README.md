# VPN Deploy Playbook
============================
A collection of Ansible Playbooks to deploy VPN services.


## Playbooks:

[x] auth.yml : setup [FreeRadius](http://freeradius.org) server for authentication and accounting
[x] pptp.yml : setup PPTP server
[x] l2tp.yml : setup IPSec/L2TP server (with pre-shared key)
[x] proxy-*.yml : setup [Shadowsocks](https://github.com/clowwindy/shadowsocks)
[ ] openvpn.yml : setup OpenVPN server
[ ] apnp-*.yml : setup APNP (Squid + Shadowsocks tunnel)


## How to use

1. install [Ansible](http://docs.ansible.com/intro_installation.html#id11) in control machine
2. copy `ansible_hosts.example` to `ansible_hosts`
3. edit the file to add your servers
4. edit files in `group_vars` or create and edit `host_vars/SERVER_NAME.yml` to fit your needs
5. run `ansible-playbook auth.yml` to setup radius server
6. run `ansible-playbook pptp.yml` to setup pptp server
7. run `ansible-playbook l2tp.yml` to setup ipsec/l2tp server
7. run `ansible-playbook openvpn.yml` to setup openvpn server

There are also some guides (in Chinese) in the [wiki](https://github.com/ftao/vpn-deploy-playbook/wiki)


## Testing

### Vagrant

Simply clone this repo and make sure you have [Vagrant](http://www.vagrantup.com) + [Virtual Box](https://www.virtualbox.org) installed and...

```vagrant up```

Vagrant is using Ubuntu 14.04 (ubuntu/trusty64) for it's OS.


