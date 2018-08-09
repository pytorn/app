#!/usr/bin/env python
# -*- coding: utf-8 -*-

from torn.api.route import Routing
import sys
sys.path.append("..")
from Controller import *

route = Routing()

# args => route, name (to be unique), Controller
route.get('/', 'index', MainController)
route.get('/{name}-reviews', 'withargs', SampleController)