#!/bin/sh
git subtree pull --prefix roles/ftao.nginx-reverse-proxy https://github.com/ftao/ansible-role-nginx-reverse-proxy.git master --squash
git subtree pull --prefix roles/ftao.nghttp2 https://github.com/ftao/ansible-role-nghttp2.git master --squash
git subtree pull --prefix roles/ftao.spdylay https://github.com/ftao/ansible-role-spdylay.git master --squash
