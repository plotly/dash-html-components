# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Video(Component):
    """A Video component.


Keyword arguments:
- children (a list of or a singular dash component, string or number; optional): The children of this component
- data-* (string; optional): A wildcard data attribute
- contentEditable (string; optional): Indicates whether the element's content is editable.
- aria-* (string; optional): A wildcard aria attribute
- height (string; optional): Specifies the height of elements listed here. For all other elements, use the CSS height property.        Note: In some instances, such as <div>, this is a legacy attribute, in which case the CSS height property should be used instead.
- className (string; optional): Often used with CSS to style elements with common properties.
- id (string; optional): The ID of this component, used to identify dash components
in callbacks. The ID needs to be unique across all of the
components in an app.
- tabIndex (string; optional): Overrides the browser's default tab order and follows the one specified instead.
- n_clicks_timestamp (number; optional): An integer that represents the time (in ms since 1970)
at which n_clicks changed. This can be used to tell
which button was changed most recently.
- style (dict; optional): Defines CSS styles which will override styles previously set.
- crossOrigin (string; optional): How the element handles cross-origin requests
- title (string; optional): Text to be displayed in a tooltip when hovering over the element.
- muted (string; optional): Indicates whether the audio will be initially silenced on page load.
- accessKey (string; optional): Defines a keyboard shortcut to activate or add focus to the element.
- controls (string; optional): Indicates whether the browser should show playback controls to the user.
- width (string; optional): For the elements listed here, this establishes the element's width.        Note: For all other instances, such as <div>, this is a legacy attribute, in which case the CSS width property should be used instead.
- role (string; optional): The ARIA role attribute
- hidden (string; optional): Prevents rendering of given element, while keeping child elements, e.g. script elements, active.
- autoPlay (string; optional): The audio or video should play as soon as possible.
- preload (string; optional): Indicates whether the whole resource, parts of it or nothing should be preloaded.
- spellCheck (string; optional): Indicates whether spell checking is allowed for the element.
- contextMenu (string; optional): Defines the ID of a <menu> element which will serve as the element's context menu.
- poster (string; optional): A URL indicating a poster frame to show until the user plays or seeks.
- key (string; optional): A unique identifier for the component, used to improve
performance by React.js while rendering components
See https://reactjs.org/docs/lists-and-keys.html for more info
- n_clicks (number; optional): An integer that represents the number of times
that this element has been clicked on.
- lang (string; optional): Defines the language used in the element.
- src (string; optional): The URL of the embeddable content.
- draggable (string; optional): Defines whether the element can be dragged.
- loop (string; optional): Indicates whether the media should start playing from the start when it's finished.
- dir (string; optional): Defines the text direction. Allowed values are ltr (Left-To-Right) or rtl (Right-To-Left)

Available events: """
    @_explicitize_args
    def __init__(self, children=None, contentEditable=Component.UNDEFINED, height=Component.UNDEFINED, draggable=Component.UNDEFINED, autoPlay=Component.UNDEFINED, n_clicks_timestamp=Component.UNDEFINED, style=Component.UNDEFINED, crossOrigin=Component.UNDEFINED, title=Component.UNDEFINED, muted=Component.UNDEFINED, accessKey=Component.UNDEFINED, controls=Component.UNDEFINED, id=Component.UNDEFINED, width=Component.UNDEFINED, role=Component.UNDEFINED, hidden=Component.UNDEFINED, tabIndex=Component.UNDEFINED, preload=Component.UNDEFINED, spellCheck=Component.UNDEFINED, contextMenu=Component.UNDEFINED, poster=Component.UNDEFINED, key=Component.UNDEFINED, n_clicks=Component.UNDEFINED, lang=Component.UNDEFINED, src=Component.UNDEFINED, className=Component.UNDEFINED, dir=Component.UNDEFINED, loop=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'data-*', 'contentEditable', 'aria-*', 'height', 'className', 'id', 'tabIndex', 'n_clicks_timestamp', 'style', 'crossOrigin', 'title', 'muted', 'accessKey', 'controls', 'width', 'role', 'hidden', 'autoPlay', 'preload', 'spellCheck', 'contextMenu', 'poster', 'key', 'n_clicks', 'lang', 'src', 'draggable', 'loop', 'dir']
        self._type = 'Video'
        self._namespace = 'dash_html_components'
        self._valid_wildcard_attributes =            ['data-', 'aria-']
        self.available_events = []
        self.available_properties = ['children', 'data-*', 'contentEditable', 'aria-*', 'height', 'className', 'id', 'tabIndex', 'n_clicks_timestamp', 'style', 'crossOrigin', 'title', 'muted', 'accessKey', 'controls', 'width', 'role', 'hidden', 'autoPlay', 'preload', 'spellCheck', 'contextMenu', 'poster', 'key', 'n_clicks', 'lang', 'src', 'draggable', 'loop', 'dir']
        self.available_wildcard_properties =            ['data-', 'aria-']

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Video, self).__init__(children=children, **args)

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
            return ('Video(' + props_string +
                   (', ' + wilds_string if wilds_string != '' else '') + ')')
        else:
            return (
                'Video(' +
                repr(getattr(self, self._prop_names[0], None)) + ')')
