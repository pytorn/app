#!/usr/bin/env python
# -*- coding: utf-8 -*-

from torn.api.route import Routing
import sys
sys.path.append("..")
from Controller import MainController, SampleController

route = Routing()

# args => route, name (to be unique), Controller
route.add('/', MainController).name('index')
route.add('/user/{name}', SampleController).args({ 'name': '[a-zA-Z]+' }).name('withargs')