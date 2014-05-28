VPN Deploy Playbook
============================
A collection of Ansible Playbooks to deploy vpn services .
Includes:
  - auth.yml : setup freeradius server for authentication and accounting.
  - pptp.yml : setup pptp server 
  - l2tp.yml : setup IPSec/L2TP server (with pre-shared key)
  - openvpn.yml : setup Openvpn server 


How to use
---------------------------
1. install [Ansible] (http://docs.ansible.com/intro_installation.html#id11) in control machine
2. copy `ansible_hosts.example` to `ansible_hosts`
3. edit the file to add your servers
4. edit files in `group_vars` or create and edit `host_vars/SERVER_NAME.yml` to fit your needs
5. run `ansible-playbook auth.yml` to setup radius server
6. run `ansible-playbook pptp.yml` to setup pptp server
7. run `ansible-playbook l2tp.yml` to setup ipsec/l2tp server
7. run `ansible-playbook openvpn.yml` to setup openvpn server

There are also some guides (in Chinese) in the [wiki](https://github.com/ftao/vpn-deploy-playbook/wiki)
