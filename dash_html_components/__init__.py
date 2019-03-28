"""Vanilla HTML components for Dash"""

from __future__ import print_function as _

import os as _os
import sys as _sys

from .version import __version__


from ._imports_ import *
from ._imports_ import __all__


_current_path = _os.path.dirname(_os.path.abspath(__file__))


_this_module = _sys.modules[__name__]


_js_dist = [
    {
        "relative_package_path": '{}.min.js'.format(__name__),
        "dev_package_path": '{}.dev.js'.format(__name__),
        "external_url": (
            "https://unpkg.com/dash-html-components@{}"
            "/dash_html_components/dash_html_components.min.js"
        ).format('0.15.0-rc1'),
        "namespace": "dash_html_components"
    }
]

_css_dist = []  # type: ignore


for _component in __all__:
    setattr(locals()[_component], '_js_dist', _js_dist)
    setattr(locals()[_component], '_css_dist', _css_dist)
