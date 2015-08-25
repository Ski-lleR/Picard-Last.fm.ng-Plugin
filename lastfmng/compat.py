# -*- coding: utf-8 -*-
try:
    from collections import OrderedDict
except ImportError:
    from .vendor.odict import OrderedDict

try:
    from ConfigParser import ConfigParser
except ImportError:
    from .vendor.ConfigParser import ConfigParser