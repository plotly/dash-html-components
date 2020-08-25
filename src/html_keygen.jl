# AUTO GENERATED FILE - DO NOT EDIT

export html_keygen

"""
    html_keygen(;kwargs...)
    html_keygen(children::Any;kwargs...)
    html_keygen(children_maker::Function;kwargs...)


A Keygen component.
Keygen is a wrapper for the <keygen> HTML5 element.
For detailed attribute info see:
https://developer.mozilla.org/en-US/docs/Web/HTML/Element/keygen
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): The children of this component
- `id` (String; optional): The ID of this component, used to identify dash components
in callbacks. The ID needs to be unique across all of the
components in an app.
- `n_clicks` (Real; optional): An integer that represents the number of times
that this element has been clicked on.
- `n_clicks_timestamp` (Real; optional): An integer that represents the time (in ms since 1970)
at which n_clicks changed. This can be used to tell
which button was changed most recently.
- `key` (String; optional): A unique identifier for the component, used to improve
performance by React.js while rendering components
See https://reactjs.org/docs/lists-and-keys.html for more info
- `role` (String; optional): The ARIA role attribute
- `data-*` (String; optional): A wildcard data attribute
- `aria-*` (String; optional): A wildcard aria attribute
- `autoFocus` (a value equal to: 'autoFocus', 'autofocus', 'AUTOFOCUS' | Bool; optional): The element should be automatically focused after the page loaded.
- `challenge` (String; optional): A challenge string that is submitted along with the public key.
- `disabled` (a value equal to: 'disabled', 'DISABLED' | Bool; optional): Indicates whether the user can interact with the element.
- `form` (String; optional): Indicates the form that is the owner of the element.
- `keyType` (String; optional): Specifies the type of key generated.
- `name` (String; optional): Name of the element. For example used by the server to identify the fields in form submits.
- `accessKey` (String; optional): Keyboard shortcut to activate or add focus to the element.
- `className` (String; optional): Often used with CSS to style elements with common properties.
- `contentEditable` (String; optional): Indicates whether the element's content is editable.
- `contextMenu` (String; optional): Defines the ID of a <menu> element which will serve as the element's context menu.
- `dir` (String; optional): Defines the text direction. Allowed values are ltr (Left-To-Right) or rtl (Right-To-Left)
- `draggable` (String; optional): Defines whether the element can be dragged.
- `hidden` (a value equal to: 'hidden', 'HIDDEN' | Bool; optional): Prevents rendering of given element, while keeping child elements, e.g. script elements, active.
- `lang` (String; optional): Defines the language used in the element.
- `spellCheck` (String; optional): Indicates whether spell checking is allowed for the element.
- `style` (Dict; optional): Defines CSS styles which will override styles previously set.
- `tabIndex` (String; optional): Overrides the browser's default tab order and follows the one specified instead.
- `title` (String; optional): Text to be displayed in a tooltip when hovering over the element.
- `loading_state` (optional): Object that holds the loading state object coming from dash-renderer. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
"""
function html_keygen(; kwargs...)
        available_props = Symbol[:children, :id, :n_clicks, :n_clicks_timestamp, :key, :role, :autoFocus, :challenge, :disabled, :form, :keyType, :name, :accessKey, :className, :contentEditable, :contextMenu, :dir, :draggable, :hidden, :lang, :spellCheck, :style, :tabIndex, :title, :loading_state]
        wild_props = Symbol[Symbol("data-"), Symbol("aria-")]
        return Component("html_keygen", "Keygen", "dash_html_components", available_props, wild_props; kwargs...)
end

html_keygen(children::Any; kwargs...) = html_keygen(;kwargs..., children = children)
html_keygen(children_maker::Function; kwargs...) = html_keygen(children_maker(); kwargs...)

