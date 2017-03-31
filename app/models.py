#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from peewee import *

db = PostgresqlDatabase('zwater', host = 'db', user = 'zwater', password = 'zwater')

class BaseModel(Model):
    class Meta:
        database = db

class Norm(BaseModel):
    acod = DecimalField()
    o1cod = DecimalField()
    o2cod = DecimalField()
    o3cod = DecimalField()
    o4cod = DecimalField()
    anh4 = DecimalField()
    o1nh4 = DecimalField()
    o2nh4 = DecimalField()
    o3nh4 = DecimalField()
    o4nh4 = DecimalField()
    ano2 = DecimalField()
    o1no2 = DecimalField()
    o2no2 = DecimalField()
    o3no2 = DecimalField()
    o4no2 = DecimalField()
    suggestion = CharField()
