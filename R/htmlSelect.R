# AUTO GENERATED FILE - DO NOT EDIT

htmlSelect <- function(..., contentEditable=NULL, n_clicks=NULL, disabled=NULL, draggable=NULL, spellCheck=NULL, children=NULL, size=NULL, n_clicks_timestamp=NULL, style=NULL, title=NULL, accessKey=NULL, id=NULL, role=NULL, hidden=NULL, tabIndex=NULL, multiple=NULL, form=NULL, contextMenu=NULL, key=NULL, autoFocus=NULL, lang=NULL, name=NULL, required=NULL, className=NULL, dir=NULL) {

    component <- list(
        props = list(contentEditable=contentEditable, n_clicks=n_clicks, disabled=disabled, draggable=draggable, spellCheck=spellCheck, children=c(children, assert_valid_children(..., wildcards = c('data-*', 'aria-*'))), size=size, n_clicks_timestamp=n_clicks_timestamp, style=style, title=title, accessKey=accessKey, id=id, role=role, hidden=hidden, tabIndex=tabIndex, multiple=multiple, form=form, contextMenu=contextMenu, key=key, autoFocus=autoFocus, lang=lang, name=name, required=required, className=className, dir=dir),
        type = 'Select',
        namespace = 'dash_html_components',
        propNames = c('contentEditable', 'n_clicks', 'disabled', 'draggable', 'spellCheck', 'children', 'size', 'n_clicks_timestamp', 'style', 'title', 'accessKey', 'id', 'role', 'hidden', 'tabIndex', 'multiple', 'form', 'contextMenu', 'key', 'autoFocus', 'lang', 'name', 'required', 'className', 'dir'),
        package = 'dashHtmlComponents'
        )

    component$props <- filter_null(component$props)
    component <- append_wildcard_props(component, wildcards = c('data-*', 'aria-*'), ...)

    structure(component, class = c('dash_component', 'list'))
}