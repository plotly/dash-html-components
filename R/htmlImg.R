# AUTO GENERATED FILE - DO NOT EDIT

htmlImg <- function(..., contentEditable=NULL, height=NULL, draggable=NULL, alt=NULL, srcSet=NULL, children=NULL, tabIndex=NULL, n_clicks_timestamp=NULL, style=NULL, crossOrigin=NULL, title=NULL, accessKey=NULL, id=NULL, width=NULL, role=NULL, useMap=NULL, hidden=NULL, spellCheck=NULL, contextMenu=NULL, key=NULL, n_clicks=NULL, lang=NULL, src=NULL, sizes=NULL, className=NULL, dir=NULL) {

    component <- list(
        props = list(contentEditable=contentEditable, height=height, draggable=draggable, alt=alt, srcSet=srcSet, children=c(children, assert_valid_children(..., wildcards = c('data-*', 'aria-*'))), tabIndex=tabIndex, n_clicks_timestamp=n_clicks_timestamp, style=style, crossOrigin=crossOrigin, title=title, accessKey=accessKey, id=id, width=width, role=role, useMap=useMap, hidden=hidden, spellCheck=spellCheck, contextMenu=contextMenu, key=key, n_clicks=n_clicks, lang=lang, src=src, sizes=sizes, className=className, dir=dir),
        type = 'Img',
        namespace = 'dash_html_components',
        propNames = c('contentEditable', 'height', 'draggable', 'alt', 'srcSet', 'children', 'tabIndex', 'n_clicks_timestamp', 'style', 'crossOrigin', 'title', 'accessKey', 'id', 'width', 'role', 'useMap', 'hidden', 'spellCheck', 'contextMenu', 'key', 'n_clicks', 'lang', 'src', 'sizes', 'className', 'dir'),
        package = 'dashHtmlComponents'
        )

    component$props <- filter_null(component$props)
    component <- append_wildcard_props(component, wildcards = c('data-*', 'aria-*'), ...)

    structure(component, class = c('dash_component', 'list'))
}