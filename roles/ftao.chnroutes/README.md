Role Name
=========
Setup static chnroutes 

Requirements
------------

Require Ubuntu 14.04 or later

Role Variables
--------------

```
chnroutes_device: 'eth0'
chnroutes_gateway: 'gateway ip address'
```


Dependencies
------------


Example Playbook
----------------

    - hosts: servers
      roles:
         - ftao.chnroutes

License
-------

GPLv3

Author Information
------------------

