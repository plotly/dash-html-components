# AUTO GENERATED FILE - DO NOT EDIT

htmlMeta <- function(..., contentEditable=NULL, draggable=NULL, children=NULL, tabIndex=NULL, n_clicks_timestamp=NULL, style=NULL, title=NULL, accessKey=NULL, id=NULL, content=NULL, httpEquiv=NULL, role=NULL, hidden=NULL, spellCheck=NULL, contextMenu=NULL, charSet=NULL, key=NULL, n_clicks=NULL, lang=NULL, name=NULL, className=NULL, dir=NULL) {

    component <- list(
        props = list(contentEditable=contentEditable, draggable=draggable, children=c(children, assert_valid_children(..., wildcards = c('data-*', 'aria-*'))), tabIndex=tabIndex, n_clicks_timestamp=n_clicks_timestamp, style=style, title=title, accessKey=accessKey, id=id, content=content, httpEquiv=httpEquiv, role=role, hidden=hidden, spellCheck=spellCheck, contextMenu=contextMenu, charSet=charSet, key=key, n_clicks=n_clicks, lang=lang, name=name, className=className, dir=dir),
        type = 'Meta',
        namespace = 'dash_html_components',
        propNames = c('contentEditable', 'draggable', 'children', 'tabIndex', 'n_clicks_timestamp', 'style', 'title', 'accessKey', 'id', 'content', 'httpEquiv', 'role', 'hidden', 'spellCheck', 'contextMenu', 'charSet', 'key', 'n_clicks', 'lang', 'name', 'className', 'dir'),
        package = 'dashHtmlComponents'
        )

    component$props <- filter_null(component$props)
    component <- append_wildcard_props(component, wildcards = c('data-*', 'aria-*'), ...)

    structure(component, class = c('dash_component', 'list'))
}