# AUTO GENERATED FILE - DO NOT EDIT

htmlForm <- function(..., children=NULL, id=NULL, n_clicks=0, n_clicks_timestamp=-1, key=NULL, role=NULL, accept=NULL, acceptCharset=NULL, action=NULL, autoComplete=NULL, encType=NULL, method=NULL, name=NULL, noValidate=NULL, target=NULL, accessKey=NULL, className=NULL, contentEditable=NULL, contextMenu=NULL, dir=NULL, draggable=NULL, hidden=NULL, lang=NULL, spellCheck=NULL, style=NULL, tabIndex=NULL, title=NULL, fireEvent=NULL, dashEvents=NULL) {

    component <- list(
      props = list(
         id=id, children=c(children, assert_valid_children(..., wildcards = c('data-*', 'aria-*'))), n_clicks=n_clicks, n_clicks_timestamp=n_clicks_timestamp, key=key, role=role, accept=accept, acceptCharset=acceptCharset, action=action, autoComplete=autoComplete, encType=encType, method=method, name=name, noValidate=noValidate, target=target, accessKey=accessKey, className=className, contentEditable=contentEditable, contextMenu=contextMenu, dir=dir, draggable=draggable, hidden=hidden, lang=lang, spellCheck=spellCheck, style=style, tabIndex=tabIndex, title=title, fireEvent=fireEvent, dashEvents=dashEvents
      ),
      type = 'Form',
      namespace = 'dash_html_components',
      propNames = c('children', 'id', 'n_clicks', 'n_clicks_timestamp', 'key', 'role', 'data-*', 'aria-*', 'accept', 'acceptCharset', 'action', 'autoComplete', 'encType', 'method', 'name', 'noValidate', 'target', 'accessKey', 'className', 'contentEditable', 'contextMenu', 'dir', 'draggable', 'hidden', 'lang', 'spellCheck', 'style', 'tabIndex', 'title'),
      package = 'dashHtmlComponents'
    )

    component$props <- filter_null(component$props)
    component <- append_wildcard_props(component, wildcards = c('data-*', 'aria-*'), ...)

    structure(component, class = c('dash_component', 'list'))
    }
