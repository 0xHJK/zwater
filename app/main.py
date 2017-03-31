#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, send_from_directory,abort, redirect

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    return 'Hello'

if __name__ == "__main__":
    # app.debug=True
    app.run(host='0.0.0.0')
