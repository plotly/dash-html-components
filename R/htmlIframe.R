# AUTO GENERATED FILE - DO NOT EDIT

htmlIframe <- function(children=NULL, contentEditable=NULL, height=NULL, draggable=NULL, tabIndex=NULL, n_clicks_timestamp=NULL, style=NULL, title=NULL, accessKey=NULL, id=NULL, width=NULL, role=NULL, hidden=NULL, spellCheck=NULL, contextMenu=NULL, key=NULL, n_clicks=NULL, lang=NULL, src=NULL, name=NULL, className=NULL, sandbox=NULL, srcDoc=NULL, dir=NULL, ...) {

    wildcard_names = names(list(...))
    
    component <- list(
        props = list(children=children, contentEditable=contentEditable, height=height, draggable=draggable, tabIndex=tabIndex, n_clicks_timestamp=n_clicks_timestamp, style=style, title=title, accessKey=accessKey, id=id, width=width, role=role, hidden=hidden, spellCheck=spellCheck, contextMenu=contextMenu, key=key, n_clicks=n_clicks, lang=lang, src=src, name=name, className=className, sandbox=sandbox, srcDoc=srcDoc, dir=dir, ...),
        type = 'Iframe',
        namespace = 'dash_html_components',
        propNames = c('children', 'contentEditable', 'height', 'draggable', 'tabIndex', 'n_clicks_timestamp', 'style', 'title', 'accessKey', 'id', 'width', 'role', 'hidden', 'spellCheck', 'contextMenu', 'key', 'n_clicks', 'lang', 'src', 'name', 'className', 'sandbox', 'srcDoc', 'dir', wildcard_names),
        package = 'dashHtmlComponents'
        )

    component$props <- filter_null(component$props)
    
    structure(component, class = c('dash_component', 'list'))    
}