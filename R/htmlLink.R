# AUTO GENERATED FILE - DO NOT EDIT

htmlLink <- function(..., contentEditable=NULL, href=NULL, draggable=NULL, integrity=NULL, children=NULL, tabIndex=NULL, n_clicks_timestamp=NULL, style=NULL, crossOrigin=NULL, title=NULL, media=NULL, accessKey=NULL, id=NULL, role=NULL, rel=NULL, hidden=NULL, spellCheck=NULL, contextMenu=NULL, key=NULL, n_clicks=NULL, lang=NULL, sizes=NULL, hrefLang=NULL, className=NULL, dir=NULL) {

    component <- list(
        props = list(contentEditable=contentEditable, href=href, draggable=draggable, integrity=integrity, children=c(children, assert_valid_children(..., wildcards = c('data-*', 'aria-*'))), tabIndex=tabIndex, n_clicks_timestamp=n_clicks_timestamp, style=style, crossOrigin=crossOrigin, title=title, media=media, accessKey=accessKey, id=id, role=role, rel=rel, hidden=hidden, spellCheck=spellCheck, contextMenu=contextMenu, key=key, n_clicks=n_clicks, lang=lang, sizes=sizes, hrefLang=hrefLang, className=className, dir=dir),
        type = 'Link',
        namespace = 'dash_html_components',
        propNames = c('contentEditable', 'href', 'draggable', 'integrity', 'children', 'tabIndex', 'n_clicks_timestamp', 'style', 'crossOrigin', 'title', 'media', 'accessKey', 'id', 'role', 'rel', 'hidden', 'spellCheck', 'contextMenu', 'key', 'n_clicks', 'lang', 'sizes', 'hrefLang', 'className', 'dir'),
        package = 'dashHtmlComponents'
        )

    component$props <- filter_null(component$props)
    component <- append_wildcard_props(component, wildcards = c('data-*', 'aria-*'), ...)

    structure(component, class = c('dash_component', 'list'))
}