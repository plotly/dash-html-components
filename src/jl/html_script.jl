# AUTO GENERATED FILE - DO NOT EDIT

export html_script

"""
    html_script(;kwargs...)
    html_script(children::Any;kwargs...)
    html_script(children_maker::Function;kwargs...)


A Script component.
Script is a wrapper for the <script> HTML5 element.

CAUTION: <script> is included for completeness, but you cannot execute
JavaScript code by providing it to a <script> element. Use a clientside
callback for this purpose instead.

For detailed attribute info see:
https://developer.mozilla.org/en-US/docs/Web/HTML/Element/script
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): The children of this component
- `id` (String; optional): The ID of this component, used to identify dash components
in callbacks. The ID needs to be unique across all of the
components in an app.
- `accessKey` (String; optional): Keyboard shortcut to activate or add focus to the element.
- `aria-*` (String; optional): A wildcard aria attribute
- `async` (a value equal to: 'async', 'ASYNC' | Bool; optional): Executes the script asynchronously.
- `charSet` (String; optional): Declares the character encoding of the page or script.
- `className` (String; optional): Often used with CSS to style elements with common properties.
- `contentEditable` (String; optional): Indicates whether the element's content is editable.
- `contextMenu` (String; optional): Defines the ID of a <menu> element which will serve as the element's context menu.
- `crossOrigin` (String; optional): How the element handles cross-origin requests
- `data-*` (String; optional): A wildcard data attribute
- `defer` (a value equal to: 'defer', 'DEFER' | Bool; optional): Indicates that the script should be executed after the page has been parsed.
- `dir` (String; optional): Defines the text direction. Allowed values are ltr (Left-To-Right) or rtl (Right-To-Left)
- `draggable` (String; optional): Defines whether the element can be dragged.
- `hidden` (a value equal to: 'hidden', 'HIDDEN' | Bool; optional): Prevents rendering of given element, while keeping child elements, e.g. script elements, active.
- `integrity` (String; optional): Specifies a Subresource Integrity value that allows browsers to verify what they fetch.
- `key` (String; optional): A unique identifier for the component, used to improve
performance by React.js while rendering components
See https://reactjs.org/docs/lists-and-keys.html for more info
- `lang` (String; optional): Defines the language used in the element.
- `loading_state` (optional): Object that holds the loading state object coming from dash-renderer. loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
- `n_clicks` (Real; optional): An integer that represents the number of times
that this element has been clicked on.
- `n_clicks_timestamp` (Real; optional): An integer that represents the time (in ms since 1970)
at which n_clicks changed. This can be used to tell
which button was changed most recently.
- `referrerPolicy` (String; optional): Specifies which referrer is sent when fetching the resource.
- `role` (String; optional): The ARIA role attribute
- `spellCheck` (String; optional): Indicates whether spell checking is allowed for the element.
- `src` (String; optional): The URL of the embeddable content.
- `style` (Dict; optional): Defines CSS styles which will override styles previously set.
- `tabIndex` (String; optional): Overrides the browser's default tab order and follows the one specified instead.
- `title` (String; optional): Text to be displayed in a tooltip when hovering over the element.
- `type` (String; optional): Defines the type of the element.
"""
function html_script(; kwargs...)
        available_props = Symbol[:children, :id, :accessKey, :async, :charSet, :className, :contentEditable, :contextMenu, :crossOrigin, :defer, :dir, :draggable, :hidden, :integrity, :key, :lang, :loading_state, :n_clicks, :n_clicks_timestamp, :referrerPolicy, :role, :spellCheck, :src, :style, :tabIndex, :title, :type]
        wild_props = Symbol[Symbol("aria-"), Symbol("data-")]
        return Component("html_script", "Script", "dash_html_components", available_props, wild_props; kwargs...)
end

html_script(children::Any; kwargs...) = html_script(;kwargs..., children = children)
html_script(children_maker::Function; kwargs...) = html_script(children_maker(); kwargs...)

