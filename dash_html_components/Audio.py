# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Audio(Component):
    """An Audio component.
Audio is a wrapper for the <audio> HTML5 element.
For detailed attribute info see:
https://developer.mozilla.org/en-US/docs/Web/HTML/Element/audio

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

- autoPlay (a value equal to: 'autoPlay', 'autoplay', 'AUTOPLAY' | boolean; optional):
    The audio or video should play as soon as possible.

- className (string; optional):
    Often used with CSS to style elements with common properties.

- contentEditable (string; optional):
    Indicates whether the element's content is editable.

- contextMenu (string; optional):
    Defines the ID of a <menu> element which will serve as the
    element's context menu.

- controls (a value equal to: 'controls', 'CONTROLS' | boolean; optional):
    Indicates whether the browser should show playback controls to the
    user.

- crossOrigin (string; optional):
    How the element handles cross-origin requests.

- data-* (string; optional):
    A wildcard data attribute.

- dir (string; optional):
    Defines the text direction. Allowed values are ltr (Left-To-Right)
    or rtl (Right-To-Left).

- draggable (string; optional):
    Defines whether the element can be dragged.

- hidden (a value equal to: 'hidden', 'HIDDEN' | boolean; optional):
    Prevents rendering of given element, while keeping child elements,
    e.g. script elements, active.

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

- loop (a value equal to: 'loop', 'LOOP' | boolean; optional):
    Indicates whether the media should start playing from the start
    when it's finished.

- muted (a value equal to: 'muted', 'MUTED' | boolean; optional):
    Indicates whether the audio will be initially silenced on page
    load.

- n_clicks (number; default 0):
    An integer that represents the number of times that this element
    has been clicked on.

- n_clicks_timestamp (number; default -1):
    An integer that represents the time (in ms since 1970) at which
    n_clicks changed. This can be used to tell which button was
    changed most recently.

- preload (string; optional):
    Indicates whether the whole resource, parts of it or nothing
    should be preloaded.

- role (string; optional):
    The ARIA role attribute.

- spellCheck (string; optional):
    Indicates whether spell checking is allowed for the element.

- src (string; optional):
    The URL of the embeddable content.

- style (dict; optional):
    Defines CSS styles which will override styles previously set.

- tabIndex (string; optional):
    Overrides the browser's default tab order and follows the one
    specified instead.

- title (string; optional):
    Text to be displayed in a tooltip when hovering over the element."""
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, n_clicks=Component.UNDEFINED, n_clicks_timestamp=Component.UNDEFINED, key=Component.UNDEFINED, role=Component.UNDEFINED, autoPlay=Component.UNDEFINED, controls=Component.UNDEFINED, crossOrigin=Component.UNDEFINED, loop=Component.UNDEFINED, muted=Component.UNDEFINED, preload=Component.UNDEFINED, src=Component.UNDEFINED, accessKey=Component.UNDEFINED, className=Component.UNDEFINED, contentEditable=Component.UNDEFINED, contextMenu=Component.UNDEFINED, dir=Component.UNDEFINED, draggable=Component.UNDEFINED, hidden=Component.UNDEFINED, lang=Component.UNDEFINED, spellCheck=Component.UNDEFINED, style=Component.UNDEFINED, tabIndex=Component.UNDEFINED, title=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'accessKey', 'aria-*', 'autoPlay', 'className', 'contentEditable', 'contextMenu', 'controls', 'crossOrigin', 'data-*', 'dir', 'draggable', 'hidden', 'key', 'lang', 'loading_state', 'loop', 'muted', 'n_clicks', 'n_clicks_timestamp', 'preload', 'role', 'spellCheck', 'src', 'style', 'tabIndex', 'title']
        self._type = 'Audio'
        self._namespace = 'dash_html_components'
        self._valid_wildcard_attributes =            ['data-', 'aria-']
        self.available_properties = ['children', 'id', 'accessKey', 'aria-*', 'autoPlay', 'className', 'contentEditable', 'contextMenu', 'controls', 'crossOrigin', 'data-*', 'dir', 'draggable', 'hidden', 'key', 'lang', 'loading_state', 'loop', 'muted', 'n_clicks', 'n_clicks_timestamp', 'preload', 'role', 'spellCheck', 'src', 'style', 'tabIndex', 'title']
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
