# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Textarea(Component):
    """A Textarea component.


Keyword arguments:
- children (a list of or a singular dash component, string or number; optional): The children of this component
- data-* (string; optional): A wildcard data attribute
- contentEditable (string; optional): Indicates whether the element's content is editable.
- aria-* (string; optional): A wildcard aria attribute
- cols (string; optional): Defines the number of columns in a textarea.
- disabled (string; optional): Indicates whether the user can interact with the element.
- className (string; optional): Often used with CSS to style elements with common properties.
- wrap (string; optional): Indicates whether the text should be wrapped.
- id (string; optional): The ID of this component, used to identify dash components
in callbacks. The ID needs to be unique across all of the
components in an app.
- tabIndex (string; optional): Overrides the browser's default tab order and follows the one specified instead.
- n_clicks_timestamp (optional): An integer that represents the time (in ms since 1970)
at which n_clicks changed. This can be used to tell
which button was changed most recently.
- style (dict; optional): Defines CSS styles which will override styles previously set.
- rows (string; optional): Defines the number of rows in a text area.
- title (string; optional): Text to be displayed in a tooltip when hovering over the element.
- autoFocus (string; optional): The element should be automatically focused after the page loaded.
- accessKey (string; optional): Defines a keyboard shortcut to activate or add focus to the element.
- role (string; optional): The ARIA role attribute
- hidden (string; optional): Prevents rendering of given element, while keeping child elements, e.g. script elements, active.
- spellCheck (string; optional): Indicates whether spell checking is allowed for the element.
- form (string; optional): Indicates the form that is the owner of the element.
- contextMenu (string; optional): Defines the ID of a <menu> element which will serve as the element's context menu.
- minLength (string; optional): Defines the minimum number of characters allowed in the element.
- readOnly (string; optional): Indicates whether the element can be edited.
- key (string; optional): A unique identifier for the component, used to improve
performance by React.js while rendering components
See https://reactjs.org/docs/lists-and-keys.html for more info
- maxLength (string; optional): Defines the maximum number of characters allowed in the element.
- n_clicks (optional): An integer that represents the number of times
that this element has been clicked on.
- placeholder (string; optional): Provides a hint to the user of what can be entered in the field.
- lang (string; optional): Defines the language used in the element.
- autoComplete (string; optional): Indicates whether controls in this form can by default have their values automatically completed by the browser.
- name (string; optional): Name of the element. For example used by the server to identify the fields in form submits.
- required (string; optional): Indicates whether this element is required to fill out or not.
- draggable (string; optional): Defines whether the element can be dragged.
- dir (string; optional): Defines the text direction. Allowed values are ltr (Left-To-Right) or rtl (Right-To-Left)

Available events: 'click'"""
    @_explicitize_args
    def __init__(self, children=None, contentEditable=Component.UNDEFINED, n_clicks=Component.UNDEFINED, cols=Component.UNDEFINED, disabled=Component.UNDEFINED, draggable=Component.UNDEFINED, wrap=Component.UNDEFINED, tabIndex=Component.UNDEFINED, n_clicks_timestamp=Component.UNDEFINED, style=Component.UNDEFINED, rows=Component.UNDEFINED, title=Component.UNDEFINED, accessKey=Component.UNDEFINED, id=Component.UNDEFINED, role=Component.UNDEFINED, hidden=Component.UNDEFINED, spellCheck=Component.UNDEFINED, form=Component.UNDEFINED, contextMenu=Component.UNDEFINED, minLength=Component.UNDEFINED, readOnly=Component.UNDEFINED, key=Component.UNDEFINED, maxLength=Component.UNDEFINED, autoFocus=Component.UNDEFINED, placeholder=Component.UNDEFINED, lang=Component.UNDEFINED, autoComplete=Component.UNDEFINED, name=Component.UNDEFINED, required=Component.UNDEFINED, className=Component.UNDEFINED, dir=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'data-*', 'contentEditable', 'aria-*', 'cols', 'disabled', 'className', 'wrap', 'id', 'tabIndex', 'n_clicks_timestamp', 'style', 'rows', 'title', 'autoFocus', 'accessKey', 'role', 'hidden', 'spellCheck', 'form', 'contextMenu', 'minLength', 'readOnly', 'key', 'maxLength', 'n_clicks', 'placeholder', 'lang', 'autoComplete', 'name', 'required', 'draggable', 'dir']
        self._type = 'Textarea'
        self._namespace = 'dash_html_components'
        self._valid_wildcard_attributes =            ['data-', 'aria-']
        self.available_events = ['click']
        self.available_properties = ['children', 'data-*', 'contentEditable', 'aria-*', 'cols', 'disabled', 'className', 'wrap', 'id', 'tabIndex', 'n_clicks_timestamp', 'style', 'rows', 'title', 'autoFocus', 'accessKey', 'role', 'hidden', 'spellCheck', 'form', 'contextMenu', 'minLength', 'readOnly', 'key', 'maxLength', 'n_clicks', 'placeholder', 'lang', 'autoComplete', 'name', 'required', 'draggable', 'dir']
        self.available_wildcard_properties =            ['data-', 'aria-']

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Textarea, self).__init__(children=children, **args)

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
            return ('Textarea(' + props_string +
                   (', ' + wilds_string if wilds_string != '' else '') + ')')
        else:
            return (
                'Textarea(' +
                repr(getattr(self, self._prop_names[0], None)) + ')')
