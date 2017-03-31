#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from peewee import *

db = PostgresqlDatabase('zwater', host = 'db', user = 'zwater', password = 'zwater')

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    """docstring for User"""
    username = CharField()
