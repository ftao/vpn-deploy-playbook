ocserv
=================

Ansible role which install and config [OpenConnect Server (ocserv)](http://www.infradead.org/ocserv/)

Requirements
------------

This role requires Ansible 1.4 or higher and only works on ubuntu platform.

Role Variables
--------------

Set domain name

```yaml
#the domain name for this server 
ocserv_domain: "{{ inventory_hostname }}"
```

Generate ceritifcate automaticlly 

```yaml
ocserv_cert_source: 'gen' #by defualt 
```

Upload ceritficate for control machine

```yaml
ocserv_cert_source: 'local'
ocserv_cert_path: '/path/to/server-cert.pem'
ocserv_cert_key_path: '/path/to/server-key.pem'
```

Use ceritficate in the server (for example, share the same ceritifcate with web server)

```
ocserv_cert_source: 'remote'
ocserv_server_cert_remote_path: '/path/to/server-cert.pem'
ocserv_server_key_remote_path: '/path/to/server-key.pem'
```

See `defaults/main.yml` for all variables
