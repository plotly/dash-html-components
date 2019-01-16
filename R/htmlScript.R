# AUTO GENERATED FILE - DO NOT EDIT

htmlScript <- function(..., defer=NULL, contentEditable=NULL, draggable=NULL, integrity=NULL, children=NULL, tabIndex=NULL, n_clicks_timestamp=NULL, style=NULL, crossOrigin=NULL, title=NULL, accessKey=NULL, id=NULL, role=NULL, hidden=NULL, type=NULL, spellCheck=NULL, contextMenu=NULL, charSet=NULL, key=NULL, n_clicks=NULL, lang=NULL, src=NULL, className=NULL, async=NULL, dir=NULL) {

    component <- list(
        props = list(defer=defer, contentEditable=contentEditable, draggable=draggable, integrity=integrity, children=c(children, assert_valid_children(..., wildcards = c('data-*', 'aria-*'))), tabIndex=tabIndex, n_clicks_timestamp=n_clicks_timestamp, style=style, crossOrigin=crossOrigin, title=title, accessKey=accessKey, id=id, role=role, hidden=hidden, type=type, spellCheck=spellCheck, contextMenu=contextMenu, charSet=charSet, key=key, n_clicks=n_clicks, lang=lang, src=src, className=className, async=async, dir=dir),
        type = 'Script',
        namespace = 'dash_html_components',
        propNames = c('defer', 'contentEditable', 'draggable', 'integrity', 'children', 'tabIndex', 'n_clicks_timestamp', 'style', 'crossOrigin', 'title', 'accessKey', 'id', 'role', 'hidden', 'type', 'spellCheck', 'contextMenu', 'charSet', 'key', 'n_clicks', 'lang', 'src', 'className', 'async', 'dir'),
        package = 'dashHtmlComponents'
        )

    component$props <- filter_null(component$props)
    component <- append_wildcard_props(component, wildcards = c('data-*', 'aria-*'), ...)

    structure(component, class = c('dash_component', 'list'))
}