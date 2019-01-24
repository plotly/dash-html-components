# AUTO GENERATED FILE - DO NOT EDIT

htmlFieldset <- function(children=NULL, contentEditable=NULL, disabled=NULL, draggable=NULL, tabIndex=NULL, n_clicks_timestamp=NULL, style=NULL, title=NULL, accessKey=NULL, id=NULL, role=NULL, hidden=NULL, spellCheck=NULL, form=NULL, contextMenu=NULL, key=NULL, n_clicks=NULL, lang=NULL, name=NULL, className=NULL, dir=NULL, ...) {

    wildcard_names = names(list(...))
    
    component <- list(
        props = list(children=children, contentEditable=contentEditable, disabled=disabled, draggable=draggable, tabIndex=tabIndex, n_clicks_timestamp=n_clicks_timestamp, style=style, title=title, accessKey=accessKey, id=id, role=role, hidden=hidden, spellCheck=spellCheck, form=form, contextMenu=contextMenu, key=key, n_clicks=n_clicks, lang=lang, name=name, className=className, dir=dir, ...),
        type = 'Fieldset',
        namespace = 'dash_html_components',
        propNames = c('children', 'contentEditable', 'disabled', 'draggable', 'tabIndex', 'n_clicks_timestamp', 'style', 'title', 'accessKey', 'id', 'role', 'hidden', 'spellCheck', 'form', 'contextMenu', 'key', 'n_clicks', 'lang', 'name', 'className', 'dir', wildcard_names),
        package = 'dashHtmlComponents'
        )

    component$props <- filter_null(component$props)
    
    structure(component, class = c('dash_component', 'list'))    
}