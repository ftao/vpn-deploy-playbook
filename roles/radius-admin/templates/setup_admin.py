#!/usr/bin/env python
'''
Setup Djra Admin User
'''
ADMIN_USER = "{{ djra_admin_user }}"
ADMIN_PASSWORD = "{{ djra_admin_password }}"

def setup_admin_user(username, password):
    from django.contrib.auth.models import User
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        user = User(username=username)
    user.set_password(password)
    user.is_superuser = True
    user.save()

setup_admin_user(ADMIN_USER, ADMIN_PASSWORD)
