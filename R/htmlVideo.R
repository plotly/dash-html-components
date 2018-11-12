# AUTO GENERATED FILE - DO NOT EDIT

htmlVideo <- function(..., children=NULL, id=NULL, n_clicks=0, n_clicks_timestamp=-1, key=NULL, role=NULL, autoPlay=NULL, controls=NULL, crossOrigin=NULL, height=NULL, loop=NULL, muted=NULL, poster=NULL, preload=NULL, src=NULL, width=NULL, accessKey=NULL, className=NULL, contentEditable=NULL, contextMenu=NULL, dir=NULL, draggable=NULL, hidden=NULL, lang=NULL, spellCheck=NULL, style=NULL, tabIndex=NULL, title=NULL, fireEvent=NULL, dashEvents=NULL) {

    component <- list(
      props = list(
         id=id, children=c(children, assert_valid_children(..., wildcards = c('data-*', 'aria-*'))), n_clicks=n_clicks, n_clicks_timestamp=n_clicks_timestamp, key=key, role=role, autoPlay=autoPlay, controls=controls, crossOrigin=crossOrigin, height=height, loop=loop, muted=muted, poster=poster, preload=preload, src=src, width=width, accessKey=accessKey, className=className, contentEditable=contentEditable, contextMenu=contextMenu, dir=dir, draggable=draggable, hidden=hidden, lang=lang, spellCheck=spellCheck, style=style, tabIndex=tabIndex, title=title, fireEvent=fireEvent, dashEvents=dashEvents
      ),
      type = 'Video',
      namespace = 'dash_html_components',
      propNames = c('children', 'id', 'n_clicks', 'n_clicks_timestamp', 'key', 'role', 'data-*', 'aria-*', 'autoPlay', 'controls', 'crossOrigin', 'height', 'loop', 'muted', 'poster', 'preload', 'src', 'width', 'accessKey', 'className', 'contentEditable', 'contextMenu', 'dir', 'draggable', 'hidden', 'lang', 'spellCheck', 'style', 'tabIndex', 'title'),
      package = 'dashHtmlComponents'
    )

    component$props <- filter_null(component$props)
    component <- append_wildcard_props(component, wildcards = c('data-*', 'aria-*'), ...)

    structure(component, class = c('dash_component', 'list'))
    }
