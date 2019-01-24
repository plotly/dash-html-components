# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Thead(Component):
    """A Thead component.


Keyword arguments:
- children (a list of or a singular dash component, string or number; optional): The children of this component
- lang (string; optional): Defines the language used in the element.
- n_clicks_timestamp (number; optional): An integer that represents the time (in ms since 1970)
at which n_clicks changed. This can be used to tell
which button was changed most recently.
- style (dict; optional): Defines CSS styles which will override styles previously set.
- data-* (string; optional): A wildcard data attribute
- contentEditable (string; optional): Indicates whether the element's content is editable.
- contextMenu (string; optional): Defines the ID of a <menu> element which will serve as the element's context menu.
- n_clicks (number; optional): An integer that represents the number of times
that this element has been clicked on.
- accessKey (string; optional): Defines a keyboard shortcut to activate or add focus to the element.
- title (string; optional): Text to be displayed in a tooltip when hovering over the element.
- aria-* (string; optional): A wildcard aria attribute
- className (string; optional): Often used with CSS to style elements with common properties.
- role (string; optional): The ARIA role attribute
- draggable (string; optional): Defines whether the element can be dragged.
- key (string; optional): A unique identifier for the component, used to improve
performance by React.js while rendering components
See https://reactjs.org/docs/lists-and-keys.html for more info
- id (string; optional): The ID of this component, used to identify dash components
in callbacks. The ID needs to be unique across all of the
components in an app.
- spellCheck (string; optional): Indicates whether spell checking is allowed for the element.
- hidden (string; optional): Prevents rendering of given element, while keeping child elements, e.g. script elements, active.
- dir (string; optional): Defines the text direction. Allowed values are ltr (Left-To-Right) or rtl (Right-To-Left)
- tabIndex (string; optional): Overrides the browser's default tab order and follows the one specified instead.

Available events: """
    @_explicitize_args
    def __init__(self, children=None, lang=Component.UNDEFINED, n_clicks_timestamp=Component.UNDEFINED, style=Component.UNDEFINED, contentEditable=Component.UNDEFINED, contextMenu=Component.UNDEFINED, accessKey=Component.UNDEFINED, title=Component.UNDEFINED, hidden=Component.UNDEFINED, className=Component.UNDEFINED, role=Component.UNDEFINED, draggable=Component.UNDEFINED, key=Component.UNDEFINED, spellCheck=Component.UNDEFINED, n_clicks=Component.UNDEFINED, id=Component.UNDEFINED, dir=Component.UNDEFINED, tabIndex=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'lang', 'n_clicks_timestamp', 'style', 'data-*', 'contentEditable', 'contextMenu', 'n_clicks', 'accessKey', 'title', 'aria-*', 'className', 'role', 'draggable', 'key', 'id', 'spellCheck', 'hidden', 'dir', 'tabIndex']
        self._type = 'Thead'
        self._namespace = 'dash_html_components'
        self._valid_wildcard_attributes =            ['data-', 'aria-']
        self.available_events = []
        self.available_properties = ['children', 'lang', 'n_clicks_timestamp', 'style', 'data-*', 'contentEditable', 'contextMenu', 'n_clicks', 'accessKey', 'title', 'aria-*', 'className', 'role', 'draggable', 'key', 'id', 'spellCheck', 'hidden', 'dir', 'tabIndex']
        self.available_wildcard_properties =            ['data-', 'aria-']

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Thead, self).__init__(children=children, **args)

    def __repr__(self):
        if(any(getattr(self, c, None) is not None
               for c in self._prop_names
               if c is not self._prop_names[0])
           or any(getattr(self, c, None) is not None
                  for c in self.__dict__.keys()
                  if any(c.startswith(wc_attr)
                  for wc_attr in self._valid_wildcard_attributes))):
            props_string = ', '.join([c+'='+repr(getattr(self, c, None))
                                      for c in self._prop_names
                                      if getattr(self, c, None) is not None])
            wilds_string = ', '.join([c+'='+repr(getattr(self, c, None))
                                      for c in self.__dict__.keys()
                                      if any([c.startswith(wc_attr)
                                      for wc_attr in
                                      self._valid_wildcard_attributes])])
            return ('Thead(' + props_string +
                   (', ' + wilds_string if wilds_string != '' else '') + ')')
        else:
            return (
                'Thead(' +
                repr(getattr(self, self._prop_names[0], None)) + ')')
