# AUTO GENERATED FILE - DO NOT EDIT

htmlA <- function(children=NULL, contentEditable=NULL, shape=NULL, href=NULL, draggable=NULL, download=NULL, tabIndex=NULL, n_clicks_timestamp=NULL, style=NULL, title=NULL, media=NULL, accessKey=NULL, id=NULL, role=NULL, rel=NULL, hidden=NULL, spellCheck=NULL, contextMenu=NULL, key=NULL, n_clicks=NULL, lang=NULL, target=NULL, hrefLang=NULL, className=NULL, dir=NULL, ...) {

    wildcard_names = names(list(...))
    
    component <- list(
        props = list(children=children, contentEditable=contentEditable, shape=shape, href=href, draggable=draggable, download=download, tabIndex=tabIndex, n_clicks_timestamp=n_clicks_timestamp, style=style, title=title, media=media, accessKey=accessKey, id=id, role=role, rel=rel, hidden=hidden, spellCheck=spellCheck, contextMenu=contextMenu, key=key, n_clicks=n_clicks, lang=lang, target=target, hrefLang=hrefLang, className=className, dir=dir, ...),
        type = 'A',
        namespace = 'dash_html_components',
        propNames = c('children', 'contentEditable', 'shape', 'href', 'draggable', 'download', 'tabIndex', 'n_clicks_timestamp', 'style', 'title', 'media', 'accessKey', 'id', 'role', 'rel', 'hidden', 'spellCheck', 'contextMenu', 'key', 'n_clicks', 'lang', 'target', 'hrefLang', 'className', 'dir', wildcard_names),
        package = 'dashHtmlComponents'
        )

    component$props <- filter_null(component$props)
    
    structure(component, class = c('dash_component', 'list'))    
}