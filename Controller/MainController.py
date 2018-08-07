#!/usr/bin/env python
# -*- coding: utf-8 -*-
from torn.api.app import Controller

class MainController(Controller):
    def get(self, request):
        return self.render("index.html", name="World")