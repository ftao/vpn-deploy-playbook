Radius-admin 
=================

Ansible role which setup a freeradius management web interface .

Requirements
------------

This role requires Ansible 1.4 or higher and only works on ubuntu platform.

Role Variables
--------------

Variables that you most likely want to change.

```yaml

#for mysql 
djra_db_name: djra
djra_db_user: djra
djra_db_password: "change-this-to-a-very-strong-password-ijjj803kJ"

djra_setup_admin: true
djra_admin_user: "admin"
djra_admin_pass: "superstrong-password-4a92e2"

```
