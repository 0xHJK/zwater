#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
from models import Norm

class NormCtrl(object):
    """docstring for NormCtrl"""
    def __init__(self, kws):
        self.acod = math.log10(kws.get('acod', 0) / 100)
        self.o1cod = math.log10(kws.get('o1cod', 0) / 100)
        self.o2cod = math.log10(kws.get('o2cod', 0) / 100)
        self.o3cod = math.log10(kws.get('o3cod', 0) / 100)
        self.o4cod = math.log10(kws.get('o4cod', 0) / 100)
        self.anh4 = math.log10(kws.get('anh4', 0) / 40)
        self.o1nh4 = math.log10(kws.get('o1nh4', 0) / 40)
        self.o2nh4 = math.log10(kws.get('o2nh4', 0) / 40)
        self.o3nh4 = math.log10(kws.get('o3nh4', 0) / 40)
        self.o4nh4 = math.log10(kws.get('o4nh4', 0) / 40)
        self.ano2 = math.log10(kws.get('ano2', 0) / 25)
        self.o1no2 = math.log10(kws.get('o1no2', 0) / 25)
        self.o2no2 = math.log10(kws.get('o2no2', 0) / 25)
        self.o3no2 = math.log10(kws.get('o3no2', 0) / 25)
        self.o4no2 = math.log10(kws.get('o4no2', 0) / 25)
        self.suggestions = []
        self.set_suggestions()
    
    def metric(self, n):
        val = math.sqrt(
            (self.acod - float(n.acod)) ** 2 +
            (self.o1cod - float(n.o1cod)) ** 2 +
            (self.o2cod - float(n.o2cod)) ** 2 +
            (self.o3cod - float(n.o3cod)) ** 2 +
            (self.o4cod - float(n.o4cod)) ** 2 +
            (self.anh4 - float(n.anh4)) ** 2 +
            (self.o1nh4 - float(n.o1nh4)) ** 2 +
            (self.o2nh4 - float(n.o2nh4)) ** 2 +
            (self.o3nh4 - float(n.o3nh4)) ** 2 +
            (self.o4nh4 - float(n.o4nh4)) ** 2 +
            (self.ano2 - float(n.ano2)) ** 2 +
            (self.o1no2 - float(n.o1no2)) ** 2 +
            (self.o2no2 - float(n.o2no2)) ** 2 +
            (self.o3no2 - float(n.o3no2)) ** 2 +
            (self.o4no2 - float(n.o4no2)) ** 2
        )
        self.suggestions.append((val, n.suggestion))

    def set_suggestions(self):
        for n in Norm.select():
            self.metric(n)

