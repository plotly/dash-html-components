# AUTO GENERATED FILE - DO NOT EDIT

htmlObjectEl <- function(children=NULL, contentEditable=NULL, height=NULL, draggable=NULL, tabIndex=NULL, n_clicks_timestamp=NULL, style=NULL, title=NULL, accessKey=NULL, id=NULL, width=NULL, role=NULL, useMap=NULL, hidden=NULL, type=NULL, spellCheck=NULL, form=NULL, contextMenu=NULL, key=NULL, n_clicks=NULL, lang=NULL, name=NULL, className=NULL, dir=NULL, ...) {

    wildcard_names = names(list(...))
    
    component <- list(
        props = list(children=children, contentEditable=contentEditable, height=height, draggable=draggable, tabIndex=tabIndex, n_clicks_timestamp=n_clicks_timestamp, style=style, title=title, accessKey=accessKey, id=id, width=width, role=role, useMap=useMap, hidden=hidden, type=type, spellCheck=spellCheck, form=form, contextMenu=contextMenu, key=key, n_clicks=n_clicks, lang=lang, name=name, className=className, dir=dir, ...),
        type = 'ObjectEl',
        namespace = 'dash_html_components',
        propNames = c('children', 'contentEditable', 'height', 'draggable', 'tabIndex', 'n_clicks_timestamp', 'style', 'title', 'accessKey', 'id', 'width', 'role', 'useMap', 'hidden', 'type', 'spellCheck', 'form', 'contextMenu', 'key', 'n_clicks', 'lang', 'name', 'className', 'dir', wildcard_names),
        package = 'dashHtmlComponents'
        )

    component$props <- filter_null(component$props)
    
    structure(component, class = c('dash_component', 'list'))    
}