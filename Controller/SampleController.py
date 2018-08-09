#!/usr/bin/env python
# -*- coding: utf-8 -*-
from torn.api import Controller

class SampleController(Controller):
    def get(self, name):
        return self.render("index.html", name = name)