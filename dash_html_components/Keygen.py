# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Keygen(Component):
    """A Keygen component.


Keyword arguments:
- children (a list of or a singular dash component, string or number; optional): The children of this component
- data-* (string; optional): A wildcard data attribute
- contentEditable (string; optional): Indicates whether the element's content is editable.
- n_clicks (optional): An integer that represents the number of times
that this element has been clicked on.
- aria-* (string; optional): A wildcard aria attribute
- disabled (string; optional): Indicates whether the user can interact with the element.
- className (string; optional): Often used with CSS to style elements with common properties.
- id (string; optional): The ID of this component, used to identify dash components
in callbacks. The ID needs to be unique across all of the
components in an app.
- tabIndex (string; optional): Overrides the browser's default tab order and follows the one specified instead.
- n_clicks_timestamp (optional): An integer that represents the time (in ms since 1970)
at which n_clicks changed. This can be used to tell
which button was changed most recently.
- style (dict; optional): Defines CSS styles which will override styles previously set.
- title (string; optional): Text to be displayed in a tooltip when hovering over the element.
- accessKey (string; optional): Defines a keyboard shortcut to activate or add focus to the element.
- role (string; optional): The ARIA role attribute
- hidden (string; optional): Prevents rendering of given element, while keeping child elements, e.g. script elements, active.
- spellCheck (string; optional): Indicates whether spell checking is allowed for the element.
- form (string; optional): Indicates the form that is the owner of the element.
- contextMenu (string; optional): Defines the ID of a <menu> element which will serve as the element's context menu.
- key (string; optional): A unique identifier for the component, used to improve
performance by React.js while rendering components
See https://reactjs.org/docs/lists-and-keys.html for more info
- autoFocus (string; optional): The element should be automatically focused after the page loaded.
- lang (string; optional): Defines the language used in the element.
- name (string; optional): Name of the element. For example used by the server to identify the fields in form submits.
- challenge (string; optional): A challenge string that is submitted along with the public key.
- draggable (string; optional): Defines whether the element can be dragged.
- keyType (string; optional): Specifies the type of key generated.
- dir (string; optional): Defines the text direction. Allowed values are ltr (Left-To-Right) or rtl (Right-To-Left)

Available events: 'click'"""
    @_explicitize_args
    def __init__(self, children=None, contentEditable=Component.UNDEFINED, n_clicks=Component.UNDEFINED, disabled=Component.UNDEFINED, draggable=Component.UNDEFINED, tabIndex=Component.UNDEFINED, n_clicks_timestamp=Component.UNDEFINED, style=Component.UNDEFINED, title=Component.UNDEFINED, accessKey=Component.UNDEFINED, id=Component.UNDEFINED, role=Component.UNDEFINED, hidden=Component.UNDEFINED, spellCheck=Component.UNDEFINED, form=Component.UNDEFINED, contextMenu=Component.UNDEFINED, key=Component.UNDEFINED, autoFocus=Component.UNDEFINED, lang=Component.UNDEFINED, name=Component.UNDEFINED, challenge=Component.UNDEFINED, className=Component.UNDEFINED, keyType=Component.UNDEFINED, dir=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'data-*', 'contentEditable', 'n_clicks', 'aria-*', 'disabled', 'className', 'id', 'tabIndex', 'n_clicks_timestamp', 'style', 'title', 'accessKey', 'role', 'hidden', 'spellCheck', 'form', 'contextMenu', 'key', 'autoFocus', 'lang', 'name', 'challenge', 'draggable', 'keyType', 'dir']
        self._type = 'Keygen'
        self._namespace = 'dash_html_components'
        self._valid_wildcard_attributes =            ['data-', 'aria-']
        self.available_events = ['click']
        self.available_properties = ['children', 'data-*', 'contentEditable', 'n_clicks', 'aria-*', 'disabled', 'className', 'id', 'tabIndex', 'n_clicks_timestamp', 'style', 'title', 'accessKey', 'role', 'hidden', 'spellCheck', 'form', 'contextMenu', 'key', 'autoFocus', 'lang', 'name', 'challenge', 'draggable', 'keyType', 'dir']
        self.available_wildcard_properties =            ['data-', 'aria-']

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Keygen, self).__init__(children=children, **args)

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
            return ('Keygen(' + props_string +
                   (', ' + wilds_string if wilds_string != '' else '') + ')')
        else:
            return (
                'Keygen(' +
                repr(getattr(self, self._prop_names[0], None)) + ')')
