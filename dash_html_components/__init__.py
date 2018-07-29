from __future__ import print_function as _

import os as _os
import sys as _sys
import dash as _dash

from ._imports_ import *
from ._imports_ import __all__
from .version import __version__


if not hasattr(_dash, 'development'):
    print("Dash was not successfully imported. Make sure you don't have a file "
          "named \n'dash.py' in your current directory.", file=_sys.stderr)
    _sys.exit(1)


_current_path = _os.path.dirname(_os.path.abspath(__file__))


_this_module = _sys.modules[__name__]


_js_dist = [
    {
        "relative_package_path": "bundle.js",
        "external_url": (
            "https://unpkg.com/dash-html-components@{}"
            "/dash_html_components/bundle.js"
        ).format(__version__),
        "namespace": "dash_html_components"
    }
]

_css_dist = []


for _component in __all__:
    setattr(locals()[_component], '_js_dist', _js_dist)
    setattr(locals()[_component], '_css_dist', _css_dist)
