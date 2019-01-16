# AUTO GENERATED FILE - DO NOT EDIT

htmlMeter <- function(children=NULL, contentEditable=NULL, high=NULL, draggable=NULL, optimum=NULL, tabIndex=NULL, n_clicks_timestamp=NULL, style=NULL, min=NULL, accessKey=NULL, id=NULL, role=NULL, low=NULL, hidden=NULL, spellCheck=NULL, form=NULL, contextMenu=NULL, max=NULL, key=NULL, n_clicks=NULL, lang=NULL, title=NULL, value=NULL, className=NULL, dir=NULL, ...) {

    wildcard_names = names(list(...))
    
    component <- list(
        props = list(children=children, contentEditable=contentEditable, high=high, draggable=draggable, optimum=optimum, tabIndex=tabIndex, n_clicks_timestamp=n_clicks_timestamp, style=style, min=min, accessKey=accessKey, id=id, role=role, low=low, hidden=hidden, spellCheck=spellCheck, form=form, contextMenu=contextMenu, max=max, key=key, n_clicks=n_clicks, lang=lang, title=title, value=value, className=className, dir=dir, ...),
        type = 'Meter',
        namespace = 'dash_html_components',
        propNames = c('children', 'contentEditable', 'high', 'draggable', 'optimum', 'tabIndex', 'n_clicks_timestamp', 'style', 'min', 'accessKey', 'id', 'role', 'low', 'hidden', 'spellCheck', 'form', 'contextMenu', 'max', 'key', 'n_clicks', 'lang', 'title', 'value', 'className', 'dir', wildcard_names),
        package = 'dashHtmlComponents'
        )

    component$props <- filter_null(component$props)
    
    structure(component, class = c('dash_component', 'list'))    
}