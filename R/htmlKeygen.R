# AUTO GENERATED FILE - DO NOT EDIT

htmlKeygen <- function(children=NULL, contentEditable=NULL, n_clicks=NULL, disabled=NULL, draggable=NULL, tabIndex=NULL, n_clicks_timestamp=NULL, style=NULL, title=NULL, accessKey=NULL, id=NULL, role=NULL, hidden=NULL, spellCheck=NULL, form=NULL, contextMenu=NULL, key=NULL, autoFocus=NULL, lang=NULL, name=NULL, challenge=NULL, className=NULL, keyType=NULL, dir=NULL, ...) {

    wildcard_names = names(list(...))
    
    component <- list(
        props = list(children=children, contentEditable=contentEditable, n_clicks=n_clicks, disabled=disabled, draggable=draggable, tabIndex=tabIndex, n_clicks_timestamp=n_clicks_timestamp, style=style, title=title, accessKey=accessKey, id=id, role=role, hidden=hidden, spellCheck=spellCheck, form=form, contextMenu=contextMenu, key=key, autoFocus=autoFocus, lang=lang, name=name, challenge=challenge, className=className, keyType=keyType, dir=dir, ...),
        type = 'Keygen',
        namespace = 'dash_html_components',
        propNames = c('children', 'contentEditable', 'n_clicks', 'disabled', 'draggable', 'tabIndex', 'n_clicks_timestamp', 'style', 'title', 'accessKey', 'id', 'role', 'hidden', 'spellCheck', 'form', 'contextMenu', 'key', 'autoFocus', 'lang', 'name', 'challenge', 'className', 'keyType', 'dir', wildcard_names),
        package = 'dashHtmlComponents'
        )

    component$props <- filter_null(component$props)
    
    structure(component, class = c('dash_component', 'list'))    
}