Role Name
=========

Setup static L2TPv3 tunnel using linux kernel .

Requirements
------------

Ubuntu 14.04 or higher 

Role Variables
--------------

A description of the settable variables for this role should go here, including any variables that are in defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role. Any variables that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well.

Dependencies
------------

None

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: clients
      roles:
         - { role: l2th-eth, l2tp_eth_session: 1, l2th_eth_cookie: 2 }

    - hosts: servers
      roles:
         - { role: username.rolename, x: 42 }
License
-------

GPLv3

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
