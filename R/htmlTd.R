# AUTO GENERATED FILE - DO NOT EDIT

htmlTd <- function(..., contentEditable=NULL, rowSpan=NULL, draggable=NULL, children=NULL, tabIndex=NULL, n_clicks_timestamp=NULL, style=NULL, title=NULL, colSpan=NULL, accessKey=NULL, id=NULL, role=NULL, hidden=NULL, spellCheck=NULL, contextMenu=NULL, key=NULL, n_clicks=NULL, lang=NULL, className=NULL, headers=NULL, dir=NULL) {

    component <- list(
        props = list(contentEditable=contentEditable, rowSpan=rowSpan, draggable=draggable, children=c(children, assert_valid_children(..., wildcards = c('data-*', 'aria-*'))), tabIndex=tabIndex, n_clicks_timestamp=n_clicks_timestamp, style=style, title=title, colSpan=colSpan, accessKey=accessKey, id=id, role=role, hidden=hidden, spellCheck=spellCheck, contextMenu=contextMenu, key=key, n_clicks=n_clicks, lang=lang, className=className, headers=headers, dir=dir),
        type = 'Td',
        namespace = 'dash_html_components',
        propNames = c('contentEditable', 'rowSpan', 'draggable', 'children', 'tabIndex', 'n_clicks_timestamp', 'style', 'title', 'colSpan', 'accessKey', 'id', 'role', 'hidden', 'spellCheck', 'contextMenu', 'key', 'n_clicks', 'lang', 'className', 'headers', 'dir'),
        package = 'dashHtmlComponents'
        )

    component$props <- filter_null(component$props)
    component <- append_wildcard_props(component, wildcards = c('data-*', 'aria-*'), ...)

    structure(component, class = c('dash_component', 'list'))
}