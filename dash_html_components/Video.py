# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Video(Component):
    """A Video component.


Keyword arguments:
- children (a list of or a singular dash component, string or number; optional): The children of this component
- id (string; optional): The ID of this component, used to identify dash components
in callbacks. The ID needs to be unique across all of the
components in an app.
- n_clicks (optional): An integer that represents the number of times
that this element has been clicked on.
- n_clicks_timestamp (optional): An integer that represents the time (in ms since 1970)
at which n_clicks changed. This can be used to tell
which button was changed most recently.
- key (string; optional): A unique identifier for the component, used to improve
performance by React.js while rendering components
See https://reactjs.org/docs/lists-and-keys.html for more info
- role (string; optional): The ARIA role attribute
- data-* (string; optional): A wildcard data attribute
- aria-* (string; optional): A wildcard aria attribute
- autoPlay (string; optional): The audio or video should play as soon as possible.
- controls (string; optional): Indicates whether the browser should show playback controls to the user.
- crossOrigin (string; optional): How the element handles cross-origin requests
- height (string; optional): Specifies the height of elements listed here. For all other elements, use the CSS height property.        Note: In some instances, such as <div>, this is a legacy attribute, in which case the CSS height property should be used instead.
- loop (string; optional): Indicates whether the media should start playing from the start when it's finished.
- muted (string; optional): Indicates whether the audio will be initially silenced on page load.
- poster (string; optional): A URL indicating a poster frame to show until the user plays or seeks.
- preload (string; optional): Indicates whether the whole resource, parts of it or nothing should be preloaded.
- src (string; optional): The URL of the embeddable content.
- width (string; optional): For the elements listed here, this establishes the element's width.        Note: For all other instances, such as <div>, this is a legacy attribute, in which case the CSS width property should be used instead.
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
    @_explicitize_args
    def __init__(self, children=None, id=Component._NO_DEFAULT_ARG, n_clicks=0, n_clicks_timestamp=-1, key=Component._NO_DEFAULT_ARG, role=Component._NO_DEFAULT_ARG, autoPlay=Component._NO_DEFAULT_ARG, controls=Component._NO_DEFAULT_ARG, crossOrigin=Component._NO_DEFAULT_ARG, height=Component._NO_DEFAULT_ARG, loop=Component._NO_DEFAULT_ARG, muted=Component._NO_DEFAULT_ARG, poster=Component._NO_DEFAULT_ARG, preload=Component._NO_DEFAULT_ARG, src=Component._NO_DEFAULT_ARG, width=Component._NO_DEFAULT_ARG, accessKey=Component._NO_DEFAULT_ARG, className=Component._NO_DEFAULT_ARG, contentEditable=Component._NO_DEFAULT_ARG, contextMenu=Component._NO_DEFAULT_ARG, dir=Component._NO_DEFAULT_ARG, draggable=Component._NO_DEFAULT_ARG, hidden=Component._NO_DEFAULT_ARG, lang=Component._NO_DEFAULT_ARG, spellCheck=Component._NO_DEFAULT_ARG, style=Component._NO_DEFAULT_ARG, tabIndex=Component._NO_DEFAULT_ARG, title=Component._NO_DEFAULT_ARG, fireEvent=Component._NO_DEFAULT_ARG, dashEvents=Component._NO_DEFAULT_ARG, **kwargs):
        self._prop_names = ['children', 'id', 'n_clicks', 'n_clicks_timestamp', 'key', 'role', 'data-*', 'aria-*', 'autoPlay', 'controls', 'crossOrigin', 'height', 'loop', 'muted', 'poster', 'preload', 'src', 'width', 'accessKey', 'className', 'contentEditable', 'contextMenu', 'dir', 'draggable', 'hidden', 'lang', 'spellCheck', 'style', 'tabIndex', 'title']
        self._type = 'Video'
        self._namespace = 'dash_html_components'
        self._valid_wildcard_attributes =            ['data-', 'aria-']
        self.available_events = ['click']
        self.available_properties = ['children', 'id', 'n_clicks', 'n_clicks_timestamp', 'key', 'role', 'data-*', 'aria-*', 'autoPlay', 'controls', 'crossOrigin', 'height', 'loop', 'muted', 'poster', 'preload', 'src', 'width', 'accessKey', 'className', 'contentEditable', 'contextMenu', 'dir', 'draggable', 'hidden', 'lang', 'spellCheck', 'style', 'tabIndex', 'title']
        self.available_wildcard_properties =            ['data-', 'aria-']

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        args = {k: _locals[k] for k in self._prop_names
                 if k != 'children' and not k.endswith('-*')}
        args.update(kwargs)  # For wildcard attrs

        for k in []:
            if k not in _explicit_args:
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
