# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


schema = {'contentEditable': {'required': False, 'type': 'string', 'nullable': False}, 'n_clicks': {'required': False, 'type': 'number', 'nullable': False}, 'cols': {'required': False, 'type': 'string', 'nullable': False}, 'disabled': {'required': False, 'type': 'string', 'nullable': False}, 'draggable': {'required': False, 'type': 'string', 'nullable': False}, 'wrap': {'required': False, 'type': 'string', 'nullable': False}, 'setProps': {'required': False, 'nullable': False}, 'children': {'required': False, 'anyof': [{'type': 'string'}, {'type': 'number'}, {'type': 'boolean'}, {'type': 'component'}, {'nullable': True, 'type': ('string', 'number'), 'allowed': [None]}, {'type': 'list', 'schema': {'anyof': [{'type': 'string'}, {'type': 'number'}, {'type': 'boolean'}, {'type': 'component'}, {'nullable': True, 'type': ('string', 'number'), 'allowed': [None]}], 'nullable': True}}], 'nullable': True}, 'tabIndex': {'required': False, 'type': 'string', 'nullable': False}, 'n_clicks_timestamp': {'required': False, 'type': 'number', 'nullable': False}, 'style': {'required': False, 'type': 'dict', 'nullable': False}, 'rows': {'required': False, 'type': 'string', 'nullable': False}, 'title': {'required': False, 'type': 'string', 'nullable': False}, 'accessKey': {'required': False, 'type': 'string', 'nullable': False}, 'dashEvents': {'required': False, 'nullable': False, 'type': ('string', 'number'), 'allowed': ['click']}, 'id': {'required': False, 'type': 'string', 'nullable': False}, 'role': {'required': False, 'type': 'string', 'nullable': False}, 'hidden': {'required': False, 'type': 'string', 'nullable': False}, 'spellCheck': {'required': False, 'type': 'string', 'nullable': False}, 'form': {'required': False, 'type': 'string', 'nullable': False}, 'contextMenu': {'required': False, 'type': 'string', 'nullable': False}, 'minLength': {'required': False, 'type': 'string', 'nullable': False}, 'readOnly': {'required': False, 'type': 'string', 'nullable': False}, 'key': {'required': False, 'type': 'string', 'nullable': False}, 'maxLength': {'required': False, 'type': 'string', 'nullable': False}, 'autoFocus': {'required': False, 'type': 'string', 'nullable': False}, 'placeholder': {'required': False, 'type': 'string', 'nullable': False}, 'fireEvent': {'required': False, 'nullable': False}, 'lang': {'required': False, 'type': 'string', 'nullable': False}, 'autoComplete': {'required': False, 'type': 'string', 'nullable': False}, 'name': {'required': False, 'type': 'string', 'nullable': False}, 'required': {'required': False, 'type': 'string', 'nullable': False}, 'className': {'required': False, 'type': 'string', 'nullable': False}, 'dir': {'required': False, 'type': 'string', 'nullable': False}}
schema = {'children': {'required': False, 'anyof': [{'type': 'string'}, {'type': 'number'}, {'type': 'boolean'}, {'type': 'component'}, {'allowed': [None], 'type': ('string', 'number'), 'nullable': True}, {'type': 'list', 'schema': {'anyof': [{'type': 'string'}, {'type': 'number'}, {'type': 'boolean'}, {'type': 'component'}, {'allowed': [None], 'type': ('string', 'number'), 'nullable': True}], 'nullable': True}}], 'nullable': True}}
class Textarea(Component):
    """A Textarea component.


Keyword arguments:
- children (string | number | boolean | dash component | a value equal to: null | list; optional): The children of this component
- id (string; optional): The ID of this component, used to identify dash components
in callbacks. The ID needs to be unique across all of the
components in an app.
- n_clicks (number; optional): An integer that represents the number of times
that this element has been clicked on.
- n_clicks_timestamp (number; optional): An integer that represents the time (in ms since 1970)
at which n_clicks changed. This can be used to tell
which button was changed most recently.
- key (string; optional): A unique identifier for the component, used to improve
performance by React.js while rendering components
See https://reactjs.org/docs/lists-and-keys.html for more info
- role (string; optional): The ARIA role attribute
- data-* (string; optional): A wildcard data attribute
- aria-* (string; optional): A wildcard aria attribute
- autoComplete (string; optional): Indicates whether controls in this form can by default have their values automatically completed by the browser.
- autoFocus (string; optional): The element should be automatically focused after the page loaded.
- cols (string; optional): Defines the number of columns in a textarea.
- disabled (string; optional): Indicates whether the user can interact with the element.
- form (string; optional): Indicates the form that is the owner of the element.
- maxLength (string; optional): Defines the maximum number of characters allowed in the element.
- minLength (string; optional): Defines the minimum number of characters allowed in the element.
- name (string; optional): Name of the element. For example used by the server to identify the fields in form submits.
- placeholder (string; optional): Provides a hint to the user of what can be entered in the field.
- readOnly (string; optional): Indicates whether the element can be edited.
- required (string; optional): Indicates whether this element is required to fill out or not.
- rows (string; optional): Defines the number of rows in a text area.
- wrap (string; optional): Indicates whether the text should be wrapped.
- accessKey (string; optional): Defines a keyboard shortcut to activate or add focus to the element.
- className (string; optional): Often used with CSS to style elements with common properties.
- contentEditable (string; optional): Indicates whether the element's content is editable.
- contextMenu (string; optional): Defines the ID of a <menu> element which will serve as the element's context menu.
- dir (string; optional): Defines the text direction. Allowed values are ltr (Left-To-Right) or rtl (Right-To-Left)
- draggable (string; optional): Defines whether the element can be dragged.
- hidden (string; optional): Prevents rendering of given element, while keeping child elements, e.g. script elements, active.
- lang (string; optional): Defines the language used in the element.
- spellCheck (string; optional): Indicates whether spell checking is allowed for the element.
- style (dict; optional): Defines CSS styles which will override styles previously set.
- tabIndex (string; optional): Overrides the browser's default tab order and follows the one specified instead.
- title (string; optional): Text to be displayed in a tooltip when hovering over the element.

Available events: 'click'"""
    _schema = schema
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, n_clicks=Component.UNDEFINED, n_clicks_timestamp=Component.UNDEFINED, key=Component.UNDEFINED, role=Component.UNDEFINED, autoComplete=Component.UNDEFINED, autoFocus=Component.UNDEFINED, cols=Component.UNDEFINED, disabled=Component.UNDEFINED, form=Component.UNDEFINED, maxLength=Component.UNDEFINED, minLength=Component.UNDEFINED, name=Component.UNDEFINED, placeholder=Component.UNDEFINED, readOnly=Component.UNDEFINED, required=Component.UNDEFINED, rows=Component.UNDEFINED, wrap=Component.UNDEFINED, accessKey=Component.UNDEFINED, className=Component.UNDEFINED, contentEditable=Component.UNDEFINED, contextMenu=Component.UNDEFINED, dir=Component.UNDEFINED, draggable=Component.UNDEFINED, hidden=Component.UNDEFINED, lang=Component.UNDEFINED, spellCheck=Component.UNDEFINED, style=Component.UNDEFINED, tabIndex=Component.UNDEFINED, title=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'n_clicks', 'n_clicks_timestamp', 'key', 'role', 'data-*', 'aria-*', 'autoComplete', 'autoFocus', 'cols', 'disabled', 'form', 'maxLength', 'minLength', 'name', 'placeholder', 'readOnly', 'required', 'rows', 'wrap', 'accessKey', 'className', 'contentEditable', 'contextMenu', 'dir', 'draggable', 'hidden', 'lang', 'spellCheck', 'style', 'tabIndex', 'title']
        self._type = 'Textarea'
        self._namespace = 'dash_html_components'
        self._valid_wildcard_attributes =            ['data-', 'aria-']
        self.available_events = ['click']
        self.available_properties = ['children', 'id', 'n_clicks', 'n_clicks_timestamp', 'key', 'role', 'data-*', 'aria-*', 'autoComplete', 'autoFocus', 'cols', 'disabled', 'form', 'maxLength', 'minLength', 'name', 'placeholder', 'readOnly', 'required', 'rows', 'wrap', 'accessKey', 'className', 'contentEditable', 'contextMenu', 'dir', 'draggable', 'hidden', 'lang', 'spellCheck', 'style', 'tabIndex', 'title']
        self.available_wildcard_properties =            ['data-', 'aria-']
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args}
        args.pop('children', None)
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
