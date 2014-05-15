Ansible - xl2tpd 
=================

Ansible role which installs and configures xl2tpd server and users.

Requirements
------------

This role requires Ansible 1.4 or higher and only works on ubuntu platform.

Role Variables
--------------

Variables that you most likely want to change.

```yaml

l2tp_network:
  local_ip: 10.9.0.1
  remote_ip: 10.9.0.30-250
  subnet: 10.9.0.0/24

#use radius servers for auth / accounting  
l2tp_use_radius: false
l2tp_radius_servers:
  - host: 127.0.0.1
    secret: some-radius-secret

#optional , add some user account
l2tp_users:
  - username: "user1"
    password: "pass1"
  - username: "user2"
    password: "passw"
```

See `defaults/main.yml` for full list of variables.

Usage 
========

1) Install xl2tp server without radius server , add a user  named `demo`

    #file l2tp.yaml
    - hosts: all
      roles:
        - role: l2tp
          l2tp_use_radius: false
          l2tp_users:
            - username: demo
            - password: demopass

2) Install xl2tp server with raidus servers

    - hosts: all
      vars:
        radius_servers:
          - host: raidus-1.exmaple.com
            secret: some-radius-secret
          - host: radisu-2.exmaple.com
            secret: some-radius-secret
      roles:
        - role: l2tp,
          l2tp_use_radius: true
          l2tp_radius_server : "{{ radius_servers }}"

Dependencies
------------

None

License
-------

GPL V3

Author Information
------------------

Tao Fei 
