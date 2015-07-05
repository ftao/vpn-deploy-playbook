ftao.nghttp2
=================

Ansible role which install nghttp2, and (optional) nghttpx service

Requirements
------------

This role requires Ansible 1.4 or higher and only works on ubuntu platform.

Role Variables
--------------

Variables that you most likely want to change.

```yaml
nghttp2_version: '1.0.2'
nghttp2_with_spdylay: false

nghttp2_enable_nghttpx: false
nghttpx_listen_port: 443
nghttpx_private_key_file: 'nghttpx.key'
nghttpx_certificate_file: 'nghttpx.cert'
```
