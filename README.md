VPN Deploy Playbook
============================
A collection of Ansible Playbooks to deploy vpn services .
Includes:
  - auth.yml : setup freeradius server for authentication and accounting.
  - pptp.yml : setup pptp server 
  - l2tp.yml : setup IPSec/L2TP server (with pre-shared key)


How to use
---------------------------
1. install [Ansible] (http://www.ansibleworks.com/docs/gettingstarted.html#id3)
2. copy `ansible_hosts.example` to `ansible_hosts`
3. edit the file to add your servers
4. edit files in `group_vars` to fit your needs
5. run `ansible-playbook auth.yml` to setup radius server
6. run `ansible-playbook pptp.yml` to setup pptp server
7. run `ansible-playbook l2tp.yml` to setup ipsec/l2tp server


Tips & Tricks
--------------------------
1. Get `Authentication failed` error message like below:

    {'msg': 'FAILED: Authentication failed.', 'failed': True}

You need set the ssh username and private key in `ansible_hosts`  or you can use *ssh-agent*  .

2. I don't want the freeradius stuff , just the pptp/l2tp server.
You can set the var `pptp_use_radius` or `l2tp_use_radius` to false by:
  * edit the vars file and set `pptp_use_radius` or `l2tp_use_radius` to `false`.
  * edit `pptp.yml` or `l2tp.yml` and set `pptp_use_radius` or `l2tp_use_radius` to `false`.


