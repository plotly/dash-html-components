# AUTO GENERATED FILE - DO NOT EDIT

htmlMeter <- function(..., contentEditable=NULL, high=NULL, draggable=NULL, optimum=NULL, children=NULL, tabIndex=NULL, n_clicks_timestamp=NULL, style=NULL, min=NULL, accessKey=NULL, id=NULL, role=NULL, low=NULL, hidden=NULL, spellCheck=NULL, form=NULL, contextMenu=NULL, max=NULL, key=NULL, n_clicks=NULL, lang=NULL, title=NULL, value=NULL, className=NULL, dir=NULL) {

    component <- list(
        props = list(contentEditable=contentEditable, high=high, draggable=draggable, optimum=optimum, children=c(children, assert_valid_children(..., wildcards = c('data-*', 'aria-*'))), tabIndex=tabIndex, n_clicks_timestamp=n_clicks_timestamp, style=style, min=min, accessKey=accessKey, id=id, role=role, low=low, hidden=hidden, spellCheck=spellCheck, form=form, contextMenu=contextMenu, max=max, key=key, n_clicks=n_clicks, lang=lang, title=title, value=value, className=className, dir=dir),
        type = 'Meter',
        namespace = 'dash_html_components',
        propNames = c('contentEditable', 'high', 'draggable', 'optimum', 'children', 'tabIndex', 'n_clicks_timestamp', 'style', 'min', 'accessKey', 'id', 'role', 'low', 'hidden', 'spellCheck', 'form', 'contextMenu', 'max', 'key', 'n_clicks', 'lang', 'title', 'value', 'className', 'dir'),
        package = 'dashHtmlComponents'
        )

    component$props <- filter_null(component$props)
    component <- append_wildcard_props(component, wildcards = c('data-*', 'aria-*'), ...)

    structure(component, class = c('dash_component', 'list'))
}