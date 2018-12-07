# AUTO GENERATED FILE - DO NOT EDIT

htmlVideo <- function(..., contentEditable=NULL, height=NULL, draggable=NULL, children=NULL, autoPlay=NULL, n_clicks_timestamp=NULL, style=NULL, crossOrigin=NULL, title=NULL, muted=NULL, accessKey=NULL, controls=NULL, id=NULL, width=NULL, role=NULL, hidden=NULL, tabIndex=NULL, preload=NULL, spellCheck=NULL, contextMenu=NULL, poster=NULL, key=NULL, n_clicks=NULL, lang=NULL, src=NULL, className=NULL, dir=NULL, loop=NULL) {

    component <- list(
        props = list(contentEditable=contentEditable, height=height, draggable=draggable, children=c(children, assert_valid_children(..., wildcards = c('data-*', 'aria-*'))), autoPlay=autoPlay, n_clicks_timestamp=n_clicks_timestamp, style=style, crossOrigin=crossOrigin, title=title, muted=muted, accessKey=accessKey, controls=controls, id=id, width=width, role=role, hidden=hidden, tabIndex=tabIndex, preload=preload, spellCheck=spellCheck, contextMenu=contextMenu, poster=poster, key=key, n_clicks=n_clicks, lang=lang, src=src, className=className, dir=dir, loop=loop),
        type = 'Video',
        namespace = 'dash_html_components',
        propNames = c('contentEditable', 'height', 'draggable', 'children', 'autoPlay', 'n_clicks_timestamp', 'style', 'crossOrigin', 'title', 'muted', 'accessKey', 'controls', 'id', 'width', 'role', 'hidden', 'tabIndex', 'preload', 'spellCheck', 'contextMenu', 'poster', 'key', 'n_clicks', 'lang', 'src', 'className', 'dir', 'loop'),
        package = 'dashHtmlComponents'
        )

    component$props <- filter_null(component$props)
    component <- append_wildcard_props(component, wildcards = c('data-*', 'aria-*'), ...)

    structure(component, class = c('dash_component', 'list'))
}