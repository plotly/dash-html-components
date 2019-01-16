# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Audio(Component):
    """A Audio component.


Keyword arguments:
- children (a list of or a singular dash component, string or number; optional): The children of this component
- data-* (string; optional): A wildcard data attribute
- contentEditable (string; optional): Indicates whether the element's content is editable.
- aria-* (string; optional): A wildcard aria attribute
- className (string; optional): Often used with CSS to style elements with common properties.
- id (string; optional): The ID of this component, used to identify dash components
in callbacks. The ID needs to be unique across all of the
components in an app.
- tabIndex (string; optional): Overrides the browser's default tab order and follows the one specified instead.
- n_clicks_timestamp (optional): An integer that represents the time (in ms since 1970)
at which n_clicks changed. This can be used to tell
which button was changed most recently.
- style (dict; optional): Defines CSS styles which will override styles previously set.
- crossOrigin (string; optional): How the element handles cross-origin requests
- title (string; optional): Text to be displayed in a tooltip when hovering over the element.
- muted (string; optional): Indicates whether the audio will be initially silenced on page load.
- accessKey (string; optional): Defines a keyboard shortcut to activate or add focus to the element.
- controls (string; optional): Indicates whether the browser should show playback controls to the user.
- role (string; optional): The ARIA role attribute
- hidden (string; optional): Prevents rendering of given element, while keeping child elements, e.g. script elements, active.
- autoPlay (string; optional): The audio or video should play as soon as possible.
- preload (string; optional): Indicates whether the whole resource, parts of it or nothing should be preloaded.
- spellCheck (string; optional): Indicates whether spell checking is allowed for the element.
- contextMenu (string; optional): Defines the ID of a <menu> element which will serve as the element's context menu.
- key (string; optional): A unique identifier for the component, used to improve
performance by React.js while rendering components
See https://reactjs.org/docs/lists-and-keys.html for more info
- n_clicks (optional): An integer that represents the number of times
that this element has been clicked on.
- lang (string; optional): Defines the language used in the element.
- src (string; optional): The URL of the embeddable content.
- draggable (string; optional): Defines whether the element can be dragged.
- dir (string; optional): Defines the text direction. Allowed values are ltr (Left-To-Right) or rtl (Right-To-Left)
- loop (string; optional): Indicates whether the media should start playing from the start when it's finished.

Available events: 'click'"""
    @_explicitize_args
    def __init__(self, children=None, contentEditable=Component.UNDEFINED, draggable=Component.UNDEFINED, autoPlay=Component.UNDEFINED, n_clicks_timestamp=Component.UNDEFINED, style=Component.UNDEFINED, crossOrigin=Component.UNDEFINED, title=Component.UNDEFINED, muted=Component.UNDEFINED, accessKey=Component.UNDEFINED, controls=Component.UNDEFINED, id=Component.UNDEFINED, role=Component.UNDEFINED, hidden=Component.UNDEFINED, tabIndex=Component.UNDEFINED, preload=Component.UNDEFINED, spellCheck=Component.UNDEFINED, contextMenu=Component.UNDEFINED, key=Component.UNDEFINED, n_clicks=Component.UNDEFINED, lang=Component.UNDEFINED, src=Component.UNDEFINED, className=Component.UNDEFINED, loop=Component.UNDEFINED, dir=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'data-*', 'contentEditable', 'aria-*', 'className', 'id', 'tabIndex', 'n_clicks_timestamp', 'style', 'crossOrigin', 'title', 'muted', 'accessKey', 'controls', 'role', 'hidden', 'autoPlay', 'preload', 'spellCheck', 'contextMenu', 'key', 'n_clicks', 'lang', 'src', 'draggable', 'dir', 'loop']
        self._type = 'Audio'
        self._namespace = 'dash_html_components'
        self._valid_wildcard_attributes =            ['data-', 'aria-']
        self.available_events = ['click']
        self.available_properties = ['children', 'data-*', 'contentEditable', 'aria-*', 'className', 'id', 'tabIndex', 'n_clicks_timestamp', 'style', 'crossOrigin', 'title', 'muted', 'accessKey', 'controls', 'role', 'hidden', 'autoPlay', 'preload', 'spellCheck', 'contextMenu', 'key', 'n_clicks', 'lang', 'src', 'draggable', 'dir', 'loop']
        self.available_wildcard_properties =            ['data-', 'aria-']

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Audio, self).__init__(children=children, **args)

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
            return ('Audio(' + props_string +
                   (', ' + wilds_string if wilds_string != '' else '') + ')')
        else:
            return (
                'Audio(' +
                repr(getattr(self, self._prop_names[0], None)) + ')')
