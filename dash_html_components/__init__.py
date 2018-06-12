from __future__ import print_function as _

import os as _os
import sys as _sys
import glob as _glob
from importlib import import_module as _import

import dash as _dash

from .version import __version__


if not hasattr(_dash, 'development'):
    print("Dash was not successfully imported. Make sure you don't have a file "
          "named \n'dash.py' in your current directory.", file=_sys.stderr)
    _sys.exit(1)

_current_path = _os.path.dirname(_os.path.abspath(__file__))

_component_files = map(
    lambda x: _os.path.splitext(_os.path.basename(x))[0],
    filter(
        lambda x: _os.path.basename(x) not in ['__init__.py', 'version.py'],
        _glob.glob(_os.path.join(_current_path, '*.py'))
    )
)

_components = [
    getattr(
        _import(".{:s}".format(c), package='dash_html_components'),
        c
    ) for c in _component_files
]

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


for _component in _components:
    setattr(_this_module, _component.__name__, _component)
    setattr(_component, '_js_dist', _js_dist)
    setattr(_component, '_css_dist', _css_dist)
