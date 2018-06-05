import collections
from dash.development.base_component import Component
import re

_VOID_ELEMENTS = [
    'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'keygen',
    'link', 'meta', 'param', 'source', 'track', 'wbr'
]

_CAMELCASE_REGEX = re.compile('([a-z0-9])([A-Z])')


def _camel_case_to_css_case(name):
    return _CAMELCASE_REGEX.sub(r'\1-\2', name).lower()


def _attribute(name, value):
    if name == 'className':
        return ('class', value,)
    elif name == 'style':
        # Dash CSS is camel-cased but CSS is hyphenated
        # convert e.g. fontColor to font-color
        inline_style = '; '.join([
            '='.join([_camel_case_to_css_case(k), v])
            for (k, v) in value.iteritems()
        ])
        return (name, inline_style,)
    else:
        return (name, value,)


def _to_html5(self):
    def __to_html5(component):
        if not isinstance(component, Component):
            return str(component)
        component_type = component._type.lower()

        children = ''
        if component_type not in _VOID_ELEMENTS:
            children = getattr(component, 'children', '')
            if isinstance(children, Component):
                children = __to_html5(children)
            elif isinstance(children, collections.MutableSequence):
                children = '\n'.join([__to_html5(child) for child in children])
            else:
                children = str(children)
            if children != '':
                children = '\n' + children

        closing = ''
        if component_type not in _VOID_ELEMENTS:
            closing = '\n</{}>'.format(component_type)

        return '<{type}{properties}>{children}{closing}'.format(
            type=component_type,
            properties=''.join([
                ' {}="{}"'.format(
                    _attribute(p, getattr(component, p)))
                for p in component._prop_names
                if (hasattr(component, p) and p is not 'children')
            ]),
            children=children,
            closing=closing)

    return __to_html5(self)
