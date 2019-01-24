# AUTO GENERATED FILE - DO NOT EDIT

htmlBlink <- function(children=NULL, lang=NULL, n_clicks_timestamp=NULL, style=NULL, contentEditable=NULL, contextMenu=NULL, accessKey=NULL, title=NULL, hidden=NULL, className=NULL, role=NULL, draggable=NULL, key=NULL, spellCheck=NULL, n_clicks=NULL, id=NULL, dir=NULL, tabIndex=NULL, ...) {

    wildcard_names = names(list(...))
    
    component <- list(
        props = list(children=children, lang=lang, n_clicks_timestamp=n_clicks_timestamp, style=style, contentEditable=contentEditable, contextMenu=contextMenu, accessKey=accessKey, title=title, hidden=hidden, className=className, role=role, draggable=draggable, key=key, spellCheck=spellCheck, n_clicks=n_clicks, id=id, dir=dir, tabIndex=tabIndex, ...),
        type = 'Blink',
        namespace = 'dash_html_components',
        propNames = c('children', 'lang', 'n_clicks_timestamp', 'style', 'contentEditable', 'contextMenu', 'accessKey', 'title', 'hidden', 'className', 'role', 'draggable', 'key', 'spellCheck', 'n_clicks', 'id', 'dir', 'tabIndex', wildcard_names),
        package = 'dashHtmlComponents'
        )

    component$props <- filter_null(component$props)
    
    structure(component, class = c('dash_component', 'list'))    
}