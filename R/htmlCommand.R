# AUTO GENERATED FILE - DO NOT EDIT

htmlCommand <- function(..., children=NULL, id=NULL, n_clicks=0, n_clicks_timestamp=-1, key=NULL, role=NULL, checked=NULL, disabled=NULL, icon=NULL, radioGroup=NULL, type=NULL, accessKey=NULL, className=NULL, contentEditable=NULL, contextMenu=NULL, dir=NULL, draggable=NULL, hidden=NULL, lang=NULL, spellCheck=NULL, style=NULL, tabIndex=NULL, title=NULL, fireEvent=NULL, dashEvents=NULL) {

    component <- list(
      props = list(
         id=id, children=c(children, assert_valid_children(..., wildcards = c('data-*', 'aria-*'))), n_clicks=n_clicks, n_clicks_timestamp=n_clicks_timestamp, key=key, role=role, checked=checked, disabled=disabled, icon=icon, radioGroup=radioGroup, type=type, accessKey=accessKey, className=className, contentEditable=contentEditable, contextMenu=contextMenu, dir=dir, draggable=draggable, hidden=hidden, lang=lang, spellCheck=spellCheck, style=style, tabIndex=tabIndex, title=title, fireEvent=fireEvent, dashEvents=dashEvents
      ),
      type = 'Command',
      namespace = 'dash_html_components',
      propNames = c('children', 'id', 'n_clicks', 'n_clicks_timestamp', 'key', 'role', 'data-*', 'aria-*', 'checked', 'disabled', 'icon', 'radioGroup', 'type', 'accessKey', 'className', 'contentEditable', 'contextMenu', 'dir', 'draggable', 'hidden', 'lang', 'spellCheck', 'style', 'tabIndex', 'title'),
      package = 'dashHtmlComponents'
    )

    component$props <- filter_null(component$props)
    component <- append_wildcard_props(component, wildcards = c('data-*', 'aria-*'), ...)

    structure(component, class = c('dash_component', 'list'))
    }
