# AUTO GENERATED FILE - DO NOT EDIT

htmlTextarea <- function(children=NULL, contentEditable=NULL, n_clicks=NULL, cols=NULL, disabled=NULL, draggable=NULL, wrap=NULL, tabIndex=NULL, n_clicks_timestamp=NULL, style=NULL, rows=NULL, title=NULL, accessKey=NULL, id=NULL, role=NULL, hidden=NULL, spellCheck=NULL, form=NULL, contextMenu=NULL, minLength=NULL, readOnly=NULL, key=NULL, maxLength=NULL, autoFocus=NULL, placeholder=NULL, lang=NULL, autoComplete=NULL, name=NULL, required=NULL, className=NULL, dir=NULL, ...) {

    wildcard_names = names(list(...))
    
    component <- list(
        props = list(children=children, contentEditable=contentEditable, n_clicks=n_clicks, cols=cols, disabled=disabled, draggable=draggable, wrap=wrap, tabIndex=tabIndex, n_clicks_timestamp=n_clicks_timestamp, style=style, rows=rows, title=title, accessKey=accessKey, id=id, role=role, hidden=hidden, spellCheck=spellCheck, form=form, contextMenu=contextMenu, minLength=minLength, readOnly=readOnly, key=key, maxLength=maxLength, autoFocus=autoFocus, placeholder=placeholder, lang=lang, autoComplete=autoComplete, name=name, required=required, className=className, dir=dir, ...),
        type = 'Textarea',
        namespace = 'dash_html_components',
        propNames = c('children', 'contentEditable', 'n_clicks', 'cols', 'disabled', 'draggable', 'wrap', 'tabIndex', 'n_clicks_timestamp', 'style', 'rows', 'title', 'accessKey', 'id', 'role', 'hidden', 'spellCheck', 'form', 'contextMenu', 'minLength', 'readOnly', 'key', 'maxLength', 'autoFocus', 'placeholder', 'lang', 'autoComplete', 'name', 'required', 'className', 'dir', wildcard_names),
        package = 'dashHtmlComponents'
        )

    component$props <- filter_null(component$props)
    
    structure(component, class = c('dash_component', 'list'))    
}