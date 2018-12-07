# AUTO GENERATED FILE - DO NOT EDIT

htmlA <- function(..., contentEditable=NULL, shape=NULL, href=NULL, draggable=NULL, download=NULL, children=NULL, tabIndex=NULL, n_clicks_timestamp=NULL, style=NULL, title=NULL, media=NULL, accessKey=NULL, id=NULL, role=NULL, rel=NULL, hidden=NULL, spellCheck=NULL, contextMenu=NULL, key=NULL, n_clicks=NULL, lang=NULL, target=NULL, hrefLang=NULL, className=NULL, dir=NULL) {

    component <- list(
        props = list(contentEditable=contentEditable, shape=shape, href=href, draggable=draggable, download=download, children=c(children, assert_valid_children(..., wildcards = c('data-*', 'aria-*'))), tabIndex=tabIndex, n_clicks_timestamp=n_clicks_timestamp, style=style, title=title, media=media, accessKey=accessKey, id=id, role=role, rel=rel, hidden=hidden, spellCheck=spellCheck, contextMenu=contextMenu, key=key, n_clicks=n_clicks, lang=lang, target=target, hrefLang=hrefLang, className=className, dir=dir),
        type = 'A',
        namespace = 'dash_html_components',
        propNames = c('contentEditable', 'shape', 'href', 'draggable', 'download', 'children', 'tabIndex', 'n_clicks_timestamp', 'style', 'title', 'media', 'accessKey', 'id', 'role', 'rel', 'hidden', 'spellCheck', 'contextMenu', 'key', 'n_clicks', 'lang', 'target', 'hrefLang', 'className', 'dir'),
        package = 'dashHtmlComponents'
        )

    component$props <- filter_null(component$props)
    component <- append_wildcard_props(component, wildcards = c('data-*', 'aria-*'), ...)

    structure(component, class = c('dash_component', 'list'))
}