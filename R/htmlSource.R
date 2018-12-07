# AUTO GENERATED FILE - DO NOT EDIT

htmlSource <- function(..., contentEditable=NULL, draggable=NULL, children=NULL, tabIndex=NULL, n_clicks_timestamp=NULL, style=NULL, title=NULL, media=NULL, accessKey=NULL, id=NULL, role=NULL, hidden=NULL, type=NULL, spellCheck=NULL, contextMenu=NULL, key=NULL, n_clicks=NULL, lang=NULL, src=NULL, sizes=NULL, className=NULL, dir=NULL) {

    component <- list(
        props = list(contentEditable=contentEditable, draggable=draggable, children=c(children, assert_valid_children(..., wildcards = c('data-*', 'aria-*'))), tabIndex=tabIndex, n_clicks_timestamp=n_clicks_timestamp, style=style, title=title, media=media, accessKey=accessKey, id=id, role=role, hidden=hidden, type=type, spellCheck=spellCheck, contextMenu=contextMenu, key=key, n_clicks=n_clicks, lang=lang, src=src, sizes=sizes, className=className, dir=dir),
        type = 'Source',
        namespace = 'dash_html_components',
        propNames = c('contentEditable', 'draggable', 'children', 'tabIndex', 'n_clicks_timestamp', 'style', 'title', 'media', 'accessKey', 'id', 'role', 'hidden', 'type', 'spellCheck', 'contextMenu', 'key', 'n_clicks', 'lang', 'src', 'sizes', 'className', 'dir'),
        package = 'dashHtmlComponents'
        )

    component$props <- filter_null(component$props)
    component <- append_wildcard_props(component, wildcards = c('data-*', 'aria-*'), ...)

    structure(component, class = c('dash_component', 'list'))
}