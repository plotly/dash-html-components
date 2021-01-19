# AUTO GENERATED FILE - DO NOT EDIT

export html_form

"""
    html_form(;kwargs...)
    html_form(children::Any;kwargs...)
    html_form(children_maker::Function;kwargs...)


A Form component.
Form is a wrapper for the <form> HTML5 element.
For detailed attribute info see:
https://developer.mozilla.org/en-US/docs/Web/HTML/Element/form
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
- `accept` (String; optional): List of types the server accepts, typically a file type.
- `acceptCharset` (String; optional): List of supported charsets.
- `action` (String; optional): The URI of a program that processes the information submitted via the form.
- `autoComplete` (String; optional): Indicates whether controls in this form can by default have their values automatically completed by the browser.
- `encType` (String; optional): Defines the content type of the form data when the method is POST.
- `method` (String; optional): Defines which HTTP method to use when submitting the form. Can be GET (default) or POST.
- `name` (String; optional): Name of the element. For example used by the server to identify the fields in form submits.
- `noValidate` (a value equal to: 'noValidate', 'novalidate', 'NOVALIDATE' | Bool; optional): This attribute indicates that the form shouldn't be validated when submitted.
- `target` (String; optional): Specifies where to open the linked document (in the case of an <a> element) or where to display the response received (in the case of a <form> element)
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
function html_form(; kwargs...)
        available_props = Symbol[:children, :id, :n_clicks, :n_clicks_timestamp, :key, :role, :accept, :acceptCharset, :action, :autoComplete, :encType, :method, :name, :noValidate, :target, :accessKey, :className, :contentEditable, :contextMenu, :dir, :draggable, :hidden, :lang, :spellCheck, :style, :tabIndex, :title, :loading_state]
        wild_props = Symbol[Symbol("data-"), Symbol("aria-")]
        return Component("html_form", "Form", "dash_html_components", available_props, wild_props; kwargs...)
end

html_form(children::Any; kwargs...) = html_form(;kwargs..., children = children)
html_form(children_maker::Function; kwargs...) = html_form(children_maker(); kwargs...)

