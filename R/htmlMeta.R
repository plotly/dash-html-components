# AUTO GENERATED FILE - DO NOT EDIT

htmlMeta <- function(children=NULL, contentEditable=NULL, draggable=NULL, tabIndex=NULL, n_clicks_timestamp=NULL, style=NULL, title=NULL, accessKey=NULL, id=NULL, content=NULL, httpEquiv=NULL, role=NULL, hidden=NULL, spellCheck=NULL, contextMenu=NULL, charSet=NULL, key=NULL, n_clicks=NULL, lang=NULL, name=NULL, className=NULL, dir=NULL, ...) {

    wildcard_names = names(list(...))
    
    component <- list(
        props = list(children=children, contentEditable=contentEditable, draggable=draggable, tabIndex=tabIndex, n_clicks_timestamp=n_clicks_timestamp, style=style, title=title, accessKey=accessKey, id=id, content=content, httpEquiv=httpEquiv, role=role, hidden=hidden, spellCheck=spellCheck, contextMenu=contextMenu, charSet=charSet, key=key, n_clicks=n_clicks, lang=lang, name=name, className=className, dir=dir, ...),
        type = 'Meta',
        namespace = 'dash_html_components',
        propNames = c('children', 'contentEditable', 'draggable', 'tabIndex', 'n_clicks_timestamp', 'style', 'title', 'accessKey', 'id', 'content', 'httpEquiv', 'role', 'hidden', 'spellCheck', 'contextMenu', 'charSet', 'key', 'n_clicks', 'lang', 'name', 'className', 'dir', wildcard_names),
        package = 'dashHtmlComponents'
        )

    component$props <- filter_null(component$props)
    
    structure(component, class = c('dash_component', 'list'))    
}