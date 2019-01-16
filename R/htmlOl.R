# AUTO GENERATED FILE - DO NOT EDIT

htmlOl <- function(children=NULL, contentEditable=NULL, draggable=NULL, tabIndex=NULL, n_clicks_timestamp=NULL, style=NULL, title=NULL, accessKey=NULL, id=NULL, start=NULL, role=NULL, hidden=NULL, spellCheck=NULL, contextMenu=NULL, reversed=NULL, key=NULL, n_clicks=NULL, lang=NULL, className=NULL, dir=NULL, ...) {

    wildcard_names = names(list(...))
    
    component <- list(
        props = list(children=children, contentEditable=contentEditable, draggable=draggable, tabIndex=tabIndex, n_clicks_timestamp=n_clicks_timestamp, style=style, title=title, accessKey=accessKey, id=id, start=start, role=role, hidden=hidden, spellCheck=spellCheck, contextMenu=contextMenu, reversed=reversed, key=key, n_clicks=n_clicks, lang=lang, className=className, dir=dir, ...),
        type = 'Ol',
        namespace = 'dash_html_components',
        propNames = c('children', 'contentEditable', 'draggable', 'tabIndex', 'n_clicks_timestamp', 'style', 'title', 'accessKey', 'id', 'start', 'role', 'hidden', 'spellCheck', 'contextMenu', 'reversed', 'key', 'n_clicks', 'lang', 'className', 'dir', wildcard_names),
        package = 'dashHtmlComponents'
        )

    component$props <- filter_null(component$props)
    
    structure(component, class = c('dash_component', 'list'))    
}