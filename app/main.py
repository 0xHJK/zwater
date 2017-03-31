#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
# from test import UserCtrl, get_users
from controller import NormCtrl

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        data = {key: float(dict(request.form)[key][0]) for key in dict(request.form)}
        print(data)
        nc = NormCtrl(data)
        print(nc.suggestions)
        msg = sorted(nc.suggestions)[0][1]
        print(nc.suggestions)
        print(msg)
        return msg

if __name__ == "__main__":
    app.debug = True
    app.run(host = '0.0.0.0')
