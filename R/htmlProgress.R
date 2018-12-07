# AUTO GENERATED FILE - DO NOT EDIT

htmlProgress <- function(..., contentEditable=NULL, draggable=NULL, children=NULL, tabIndex=NULL, n_clicks_timestamp=NULL, style=NULL, title=NULL, accessKey=NULL, id=NULL, role=NULL, hidden=NULL, spellCheck=NULL, form=NULL, contextMenu=NULL, max=NULL, key=NULL, n_clicks=NULL, lang=NULL, value=NULL, className=NULL, dir=NULL) {

    component <- list(
        props = list(contentEditable=contentEditable, draggable=draggable, children=c(children, assert_valid_children(..., wildcards = c('data-*', 'aria-*'))), tabIndex=tabIndex, n_clicks_timestamp=n_clicks_timestamp, style=style, title=title, accessKey=accessKey, id=id, role=role, hidden=hidden, spellCheck=spellCheck, form=form, contextMenu=contextMenu, max=max, key=key, n_clicks=n_clicks, lang=lang, value=value, className=className, dir=dir),
        type = 'Progress',
        namespace = 'dash_html_components',
        propNames = c('contentEditable', 'draggable', 'children', 'tabIndex', 'n_clicks_timestamp', 'style', 'title', 'accessKey', 'id', 'role', 'hidden', 'spellCheck', 'form', 'contextMenu', 'max', 'key', 'n_clicks', 'lang', 'value', 'className', 'dir'),
        package = 'dashHtmlComponents'
        )

    component$props <- filter_null(component$props)
    component <- append_wildcard_props(component, wildcards = c('data-*', 'aria-*'), ...)

    structure(component, class = c('dash_component', 'list'))
}