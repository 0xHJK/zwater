#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from models import User

class UserCtrl(object):
    """docstring for UserCtrl"""
    def __init__(self, username):
        super(UserCtrl, self).__init__()
        User.create_table(fail_silently=True)
        User.create(username = username)

def get_users():
    for u in User.select():
        yield u.username
