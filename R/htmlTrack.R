# AUTO GENERATED FILE - DO NOT EDIT

htmlTrack <- function(..., contentEditable=NULL, draggable=NULL, id=NULL, children=NULL, tabIndex=NULL, n_clicks_timestamp=NULL, style=NULL, title=NULL, accessKey=NULL, label=NULL, role=NULL, srcLang=NULL, hidden=NULL, spellCheck=NULL, contextMenu=NULL, key=NULL, n_clicks=NULL, lang=NULL, src=NULL, kind=NULL, default=NULL, className=NULL, dir=NULL) {

    component <- list(
        props = list(contentEditable=contentEditable, draggable=draggable, id=id, children=c(children, assert_valid_children(..., wildcards = c('data-*', 'aria-*'))), tabIndex=tabIndex, n_clicks_timestamp=n_clicks_timestamp, style=style, title=title, accessKey=accessKey, label=label, role=role, srcLang=srcLang, hidden=hidden, spellCheck=spellCheck, contextMenu=contextMenu, key=key, n_clicks=n_clicks, lang=lang, src=src, kind=kind, default=default, className=className, dir=dir),
        type = 'Track',
        namespace = 'dash_html_components',
        propNames = c('contentEditable', 'draggable', 'id', 'children', 'tabIndex', 'n_clicks_timestamp', 'style', 'title', 'accessKey', 'label', 'role', 'srcLang', 'hidden', 'spellCheck', 'contextMenu', 'key', 'n_clicks', 'lang', 'src', 'kind', 'default', 'className', 'dir'),
        package = 'dashHtmlComponents'
        )

    component$props <- filter_null(component$props)
    component <- append_wildcard_props(component, wildcards = c('data-*', 'aria-*'), ...)

    structure(component, class = c('dash_component', 'list'))
}