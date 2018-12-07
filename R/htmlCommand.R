# AUTO GENERATED FILE - DO NOT EDIT

htmlCommand <- function(..., contentEditable=NULL, disabled=NULL, className=NULL, children=NULL, tabIndex=NULL, n_clicks_timestamp=NULL, style=NULL, checked=NULL, title=NULL, accessKey=NULL, id=NULL, role=NULL, hidden=NULL, type=NULL, spellCheck=NULL, contextMenu=NULL, key=NULL, n_clicks=NULL, icon=NULL, lang=NULL, draggable=NULL, radioGroup=NULL, dir=NULL) {

    component <- list(
        props = list(contentEditable=contentEditable, disabled=disabled, className=className, children=c(children, assert_valid_children(..., wildcards = c('data-*', 'aria-*'))), tabIndex=tabIndex, n_clicks_timestamp=n_clicks_timestamp, style=style, checked=checked, title=title, accessKey=accessKey, id=id, role=role, hidden=hidden, type=type, spellCheck=spellCheck, contextMenu=contextMenu, key=key, n_clicks=n_clicks, icon=icon, lang=lang, draggable=draggable, radioGroup=radioGroup, dir=dir),
        type = 'Command',
        namespace = 'dash_html_components',
        propNames = c('contentEditable', 'disabled', 'className', 'children', 'tabIndex', 'n_clicks_timestamp', 'style', 'checked', 'title', 'accessKey', 'id', 'role', 'hidden', 'type', 'spellCheck', 'contextMenu', 'key', 'n_clicks', 'icon', 'lang', 'draggable', 'radioGroup', 'dir'),
        package = 'dashHtmlComponents'
        )

    component$props <- filter_null(component$props)
    component <- append_wildcard_props(component, wildcards = c('data-*', 'aria-*'), ...)

    structure(component, class = c('dash_component', 'list'))
}