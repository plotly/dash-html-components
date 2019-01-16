filter_null <- function(x) {
	  if (length(x) == 0 || !is.list(x)) return(x)
  x[!vapply(x, is.null, logical(1))]
}

assert_valid_children <- function(..., wildcards = NULL) {
	  kids <- list(...)
  if (length(wildcards)) {
	      pattern <- paste(paste0('^', wildcards), collapse = '|')
      kids <- kids[!grepl(pattern, names2(kids))]
        }
    if (!length(kids)) return(NULL)
    assert_no_names(kids)
}

append_wildcard_props <- function(component, wildcards = NULL, ...) {
	  attrs <- list(...)
  if (!length(attrs) || !length(wildcards)) return(component)
    pattern <- paste(paste0('^', wildcards), collapse = '|')
    attrs_wild <- attrs[grepl(pattern, names2(attrs))]
      if (!length(attrs_wild)) return(component)
      component[['props']] <- c(component[['props']] %||% list(), attrs_wild)
        component[['propNames']] <- c(component[['propNames']], names(attrs_wild))
        component
}

names2 <- function(x) names(x) %||% rep('', length(x))

`%||%` <- function(x, y) if (length(x)) x else y

assert_no_names <- function(x) {
	  nms <- names(x)
  if (is.null(nms)) return(x)
    if (identical('', unique(nms))) return(setNames(x, NULL))
    stop(
	     sprintf(
		           "Didn't recognize the following named arguments: '%s'",
			         paste(nms, collapse = "', '")
			       ), call. = FALSE
	       )
}
