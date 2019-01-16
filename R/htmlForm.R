# AUTO GENERATED FILE - DO NOT EDIT

htmlForm <- function(children=NULL, contentEditable=NULL, accept=NULL, autoComplete=NULL, draggable=NULL, tabIndex=NULL, n_clicks_timestamp=NULL, style=NULL, title=NULL, accessKey=NULL, id=NULL, role=NULL, hidden=NULL, method=NULL, spellCheck=NULL, contextMenu=NULL, key=NULL, n_clicks=NULL, target=NULL, lang=NULL, name=NULL, className=NULL, noValidate=NULL, action=NULL, acceptCharset=NULL, dir=NULL, encType=NULL, ...) {

    wildcard_names = names(list(...))
    
    component <- list(
        props = list(children=children, contentEditable=contentEditable, accept=accept, autoComplete=autoComplete, draggable=draggable, tabIndex=tabIndex, n_clicks_timestamp=n_clicks_timestamp, style=style, title=title, accessKey=accessKey, id=id, role=role, hidden=hidden, method=method, spellCheck=spellCheck, contextMenu=contextMenu, key=key, n_clicks=n_clicks, target=target, lang=lang, name=name, className=className, noValidate=noValidate, action=action, acceptCharset=acceptCharset, dir=dir, encType=encType, ...),
        type = 'Form',
        namespace = 'dash_html_components',
        propNames = c('children', 'contentEditable', 'accept', 'autoComplete', 'draggable', 'tabIndex', 'n_clicks_timestamp', 'style', 'title', 'accessKey', 'id', 'role', 'hidden', 'method', 'spellCheck', 'contextMenu', 'key', 'n_clicks', 'target', 'lang', 'name', 'className', 'noValidate', 'action', 'acceptCharset', 'dir', 'encType', wildcard_names),
        package = 'dashHtmlComponents'
        )

    component$props <- filter_null(component$props)
    
    structure(component, class = c('dash_component', 'list'))    
}