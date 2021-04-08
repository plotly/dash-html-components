# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Textarea(Component):
    """A Textarea component.
Textarea is a wrapper for the <textarea> HTML5 element.
For detailed attribute info see:
https://developer.mozilla.org/en-US/docs/Web/HTML/Element/textarea

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    The children of this component.

- id (string; optional):
    The ID of this component, used to identify dash components in
    callbacks. The ID needs to be unique across all of the components
    in an app.

- accessKey (string; optional):
    Keyboard shortcut to activate or add focus to the element.

- aria-* (string; optional):
    A wildcard aria attribute.

- autoComplete (string; optional):
    Indicates whether controls in this form can by default have their
    values automatically completed by the browser.

- autoFocus (a value equal to: 'autoFocus', 'autofocus', 'AUTOFOCUS' | boolean; optional):
    The element should be automatically focused after the page loaded.

- className (string; optional):
    Often used with CSS to style elements with common properties.

- cols (string | number; optional):
    Defines the number of columns in a textarea.

- contentEditable (string; optional):
    Indicates whether the element's content is editable.

- contextMenu (string; optional):
    Defines the ID of a <menu> element which will serve as the
    element's context menu.

- data-* (string; optional):
    A wildcard data attribute.

- dir (string; optional):
    Defines the text direction. Allowed values are ltr (Left-To-Right)
    or rtl (Right-To-Left).

- disabled (a value equal to: 'disabled', 'DISABLED' | boolean; optional):
    Indicates whether the user can interact with the element.

- draggable (string; optional):
    Defines whether the element can be dragged.

- form (string; optional):
    Indicates the form that is the owner of the element.

- hidden (a value equal to: 'hidden', 'HIDDEN' | boolean; optional):
    Prevents rendering of given element, while keeping child elements,
    e.g. script elements, active.

- inputMode (string; optional):
    Provides a hint as to the type of data that might be entered by
    the user while editing the element or its contents. The attribute
    can be used with form controls (such as the value of textarea
    elements), or in elements in an editing host (e.g., using
    contenteditable attribute).

- key (string; optional):
    A unique identifier for the component, used to improve performance
    by React.js while rendering components See
    https://reactjs.org/docs/lists-and-keys.html for more info.

- lang (string; optional):
    Defines the language used in the element.

- loading_state (dict; optional):
    Object that holds the loading state object coming from
    dash-renderer.

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- maxLength (string | number; optional):
    Defines the maximum number of characters allowed in the element.

- minLength (string | number; optional):
    Defines the minimum number of characters allowed in the element.

- n_clicks (number; default 0):
    An integer that represents the number of times that this element
    has been clicked on.

- n_clicks_timestamp (number; default -1):
    An integer that represents the time (in ms since 1970) at which
    n_clicks changed. This can be used to tell which button was
    changed most recently.

- name (string; optional):
    Name of the element. For example used by the server to identify
    the fields in form submits.

- placeholder (string; optional):
    Provides a hint to the user of what can be entered in the field.

- readOnly (string; optional):
    Indicates whether the element can be edited.

- required (a value equal to: 'required', 'REQUIRED' | boolean; optional):
    Indicates whether this element is required to fill out or not.

- role (string; optional):
    The ARIA role attribute.

- rows (string | number; optional):
    Defines the number of rows in a text area.

- spellCheck (string; optional):
    Indicates whether spell checking is allowed for the element.

- style (dict; optional):
    Defines CSS styles which will override styles previously set.

- tabIndex (string; optional):
    Overrides the browser's default tab order and follows the one
    specified instead.

- title (string; optional):
    Text to be displayed in a tooltip when hovering over the element.

- wrap (string; optional):
    Indicates whether the text should be wrapped."""
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, n_clicks=Component.UNDEFINED, n_clicks_timestamp=Component.UNDEFINED, key=Component.UNDEFINED, role=Component.UNDEFINED, autoComplete=Component.UNDEFINED, autoFocus=Component.UNDEFINED, cols=Component.UNDEFINED, disabled=Component.UNDEFINED, form=Component.UNDEFINED, inputMode=Component.UNDEFINED, maxLength=Component.UNDEFINED, minLength=Component.UNDEFINED, name=Component.UNDEFINED, placeholder=Component.UNDEFINED, readOnly=Component.UNDEFINED, required=Component.UNDEFINED, rows=Component.UNDEFINED, wrap=Component.UNDEFINED, accessKey=Component.UNDEFINED, className=Component.UNDEFINED, contentEditable=Component.UNDEFINED, contextMenu=Component.UNDEFINED, dir=Component.UNDEFINED, draggable=Component.UNDEFINED, hidden=Component.UNDEFINED, lang=Component.UNDEFINED, spellCheck=Component.UNDEFINED, style=Component.UNDEFINED, tabIndex=Component.UNDEFINED, title=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'accessKey', 'aria-*', 'autoComplete', 'autoFocus', 'className', 'cols', 'contentEditable', 'contextMenu', 'data-*', 'dir', 'disabled', 'draggable', 'form', 'hidden', 'inputMode', 'key', 'lang', 'loading_state', 'maxLength', 'minLength', 'n_clicks', 'n_clicks_timestamp', 'name', 'placeholder', 'readOnly', 'required', 'role', 'rows', 'spellCheck', 'style', 'tabIndex', 'title', 'wrap']
        self._type = 'Textarea'
        self._namespace = 'dash_html_components'
        self._valid_wildcard_attributes =            ['data-', 'aria-']
        self.available_properties = ['children', 'id', 'accessKey', 'aria-*', 'autoComplete', 'autoFocus', 'className', 'cols', 'contentEditable', 'contextMenu', 'data-*', 'dir', 'disabled', 'draggable', 'form', 'hidden', 'inputMode', 'key', 'lang', 'loading_state', 'maxLength', 'minLength', 'n_clicks', 'n_clicks_timestamp', 'name', 'placeholder', 'readOnly', 'required', 'role', 'rows', 'spellCheck', 'style', 'tabIndex', 'title', 'wrap']
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
