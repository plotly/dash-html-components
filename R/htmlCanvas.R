# AUTO GENERATED FILE - DO NOT EDIT

htmlCanvas <- function(..., contentEditable=NULL, height=NULL, draggable=NULL, children=NULL, tabIndex=NULL, n_clicks_timestamp=NULL, style=NULL, title=NULL, accessKey=NULL, id=NULL, width=NULL, role=NULL, hidden=NULL, spellCheck=NULL, contextMenu=NULL, key=NULL, n_clicks=NULL, lang=NULL, className=NULL, dir=NULL) {

    component <- list(
        props = list(contentEditable=contentEditable, height=height, draggable=draggable, children=c(children, assert_valid_children(..., wildcards = c('data-*', 'aria-*'))), tabIndex=tabIndex, n_clicks_timestamp=n_clicks_timestamp, style=style, title=title, accessKey=accessKey, id=id, width=width, role=role, hidden=hidden, spellCheck=spellCheck, contextMenu=contextMenu, key=key, n_clicks=n_clicks, lang=lang, className=className, dir=dir),
        type = 'Canvas',
        namespace = 'dash_html_components',
        propNames = c('contentEditable', 'height', 'draggable', 'children', 'tabIndex', 'n_clicks_timestamp', 'style', 'title', 'accessKey', 'id', 'width', 'role', 'hidden', 'spellCheck', 'contextMenu', 'key', 'n_clicks', 'lang', 'className', 'dir'),
        package = 'dashHtmlComponents'
        )

    component$props <- filter_null(component$props)
    component <- append_wildcard_props(component, wildcards = c('data-*', 'aria-*'), ...)

    structure(component, class = c('dash_component', 'list'))
}