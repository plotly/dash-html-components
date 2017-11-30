import collections
from dash.development.base_component import Component

_VOID_ELEMENTS = [
    'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'keygen',
    'link', 'meta', 'param', 'source', 'track', 'wbr'
]


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
                ' {name}="{value}"'.format(
                    name=p, value=getattr(component, p))
                for p in component._prop_names
                if (hasattr(component, p) and p is not 'children')
            ]),
            children=children,
            closing=closing)

    return __to_html5(self)
