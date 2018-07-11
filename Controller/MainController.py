#!/usr/bin/env python
# -*- coding: utf-8 -*-
from torn.api.app import Controller

class MainController(Controller):
    def index():
        return "<h1>Hello World</h1>"