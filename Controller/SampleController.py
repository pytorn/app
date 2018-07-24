#!/usr/bin/env python
# -*- coding: utf-8 -*-
from torn.api.app import Controller

class SampleController(Controller):
    def get(self, name):
        return name