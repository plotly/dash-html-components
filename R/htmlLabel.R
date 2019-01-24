# AUTO GENERATED FILE - DO NOT EDIT

htmlLabel <- function(children=NULL, contentEditable=NULL, draggable=NULL, tabIndex=NULL, n_clicks_timestamp=NULL, style=NULL, htmlFor=NULL, accessKey=NULL, id=NULL, role=NULL, hidden=NULL, spellCheck=NULL, form=NULL, contextMenu=NULL, key=NULL, n_clicks=NULL, lang=NULL, title=NULL, className=NULL, dir=NULL, ...) {

    wildcard_names = names(list(...))
    
    component <- list(
        props = list(children=children, contentEditable=contentEditable, draggable=draggable, tabIndex=tabIndex, n_clicks_timestamp=n_clicks_timestamp, style=style, htmlFor=htmlFor, accessKey=accessKey, id=id, role=role, hidden=hidden, spellCheck=spellCheck, form=form, contextMenu=contextMenu, key=key, n_clicks=n_clicks, lang=lang, title=title, className=className, dir=dir, ...),
        type = 'Label',
        namespace = 'dash_html_components',
        propNames = c('children', 'contentEditable', 'draggable', 'tabIndex', 'n_clicks_timestamp', 'style', 'htmlFor', 'accessKey', 'id', 'role', 'hidden', 'spellCheck', 'form', 'contextMenu', 'key', 'n_clicks', 'lang', 'title', 'className', 'dir', wildcard_names),
        package = 'dashHtmlComponents'
        )

    component$props <- filter_null(component$props)
    
    structure(component, class = c('dash_component', 'list'))    
}