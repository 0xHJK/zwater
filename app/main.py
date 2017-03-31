#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask
from test import UserCtrl, get_users

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    u1 = UserCtrl('tom')
    u2 = UserCtrl('jack')
    return ' '.join(get_users())

if __name__ == "__main__":
    app.debug = True
    app.run(host = '0.0.0.0')
