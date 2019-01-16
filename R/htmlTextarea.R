# AUTO GENERATED FILE - DO NOT EDIT

htmlTextarea <- function(..., contentEditable=NULL, n_clicks=NULL, cols=NULL, disabled=NULL, draggable=NULL, wrap=NULL, children=NULL, tabIndex=NULL, n_clicks_timestamp=NULL, style=NULL, rows=NULL, title=NULL, accessKey=NULL, id=NULL, role=NULL, hidden=NULL, spellCheck=NULL, form=NULL, contextMenu=NULL, minLength=NULL, readOnly=NULL, key=NULL, maxLength=NULL, autoFocus=NULL, placeholder=NULL, lang=NULL, autoComplete=NULL, name=NULL, required=NULL, className=NULL, dir=NULL) {

    component <- list(
        props = list(contentEditable=contentEditable, n_clicks=n_clicks, cols=cols, disabled=disabled, draggable=draggable, wrap=wrap, children=c(children, assert_valid_children(..., wildcards = c('data-*', 'aria-*'))), tabIndex=tabIndex, n_clicks_timestamp=n_clicks_timestamp, style=style, rows=rows, title=title, accessKey=accessKey, id=id, role=role, hidden=hidden, spellCheck=spellCheck, form=form, contextMenu=contextMenu, minLength=minLength, readOnly=readOnly, key=key, maxLength=maxLength, autoFocus=autoFocus, placeholder=placeholder, lang=lang, autoComplete=autoComplete, name=name, required=required, className=className, dir=dir),
        type = 'Textarea',
        namespace = 'dash_html_components',
        propNames = c('contentEditable', 'n_clicks', 'cols', 'disabled', 'draggable', 'wrap', 'children', 'tabIndex', 'n_clicks_timestamp', 'style', 'rows', 'title', 'accessKey', 'id', 'role', 'hidden', 'spellCheck', 'form', 'contextMenu', 'minLength', 'readOnly', 'key', 'maxLength', 'autoFocus', 'placeholder', 'lang', 'autoComplete', 'name', 'required', 'className', 'dir'),
        package = 'dashHtmlComponents'
        )

    component$props <- filter_null(component$props)
    component <- append_wildcard_props(component, wildcards = c('data-*', 'aria-*'), ...)

    structure(component, class = c('dash_component', 'list'))
}