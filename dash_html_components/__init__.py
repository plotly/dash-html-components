"""Vanilla HTML components for Dash"""

from __future__ import print_function as _

import os as _os
import sys as _sys
import dash as _dash
import json as _json

from .version import __version__  # noqa: F401

# Module imports trigger a dash.development import, need to check this first
if not hasattr(_dash, 'development'):
    print(
        "Dash was not successfully imported. Make sure you don't have a file "
        "named \n'dash.py' in your current directory.", file=_sys.stderr)
    _sys.exit(1)

# Must update to dash>=0.22.0 to use this version of dash-html-components
if not hasattr(_dash.development.base_component, '_explicitize_args'):
    print("Please update the `dash` module to >= 0.22.0 to use this "
          "version of dash_html_components.\n"
          "You are using version {:s}".format(_dash.version.__version__),
          file=_sys.stderr)
    _sys.exit(1)


from ._imports_ import *  # noqa: F403
from ._imports_ import __all__


_current_path = _os.path.dirname(_os.path.abspath(__file__))


_this_module = _sys.modules[__name__]

_basepath = _os.path.dirname(__file__)
_filepath = _os.path.abspath(_os.path.join(_basepath, 'package.json'))
with open(_filepath) as _f:
    _package = _json.load(_f)

_js_package_name = _package['name']
_py_package_name = __name__
_js_version = _package['version']

_js_dist = [
    {
        "relative_package_path": '{}.min.js'.format(_py_package_name),
        "dev_package_path": '{}.dev.js'.format(_py_package_name),
        "external_url": (
            "https://unpkg.com/{0}@{1}/{2}/{2}.min.js"
        ).format(_js_package_name, _js_version, _py_package_name),
        "namespace": _py_package_name
    }
]

_css_dist = []


for _component in __all__:
    setattr(locals()[_component], '_js_dist', _js_dist)
    setattr(locals()[_component], '_css_dist', _css_dist)
