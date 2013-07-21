VPN Deploy Playbook
============================
A collection of Ansible Playbook to deply vpn services .

roles:

- common
- db
- auth
- pptp
- l2tp


How to use
---------------------------
1. install Ansible
2. copy `ansible_hosts.example`  to `ansible_hosts`
3. edit the file to add your servers
4. edit files in `group_vars` to fit your needs
5. run ansible-playbook auth.yml to setup radius server
6. run ansible-playbook pptp.yml to setup pptp server 
7. run ansible-playbook l2tp.yml to setup ipsec/l2tp server 


