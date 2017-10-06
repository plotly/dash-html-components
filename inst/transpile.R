if (!require(dashTranspileR)) remotes::install_github("plotly/dashTranspileR")

library(dashTranspileR)

html <- transpile()

# add a link to the description section (currently no description is provided)
desc <- paste0("#' @description See <https://developer.mozilla.org/en-US/docs/Web/HTML/Element/", tolower(html$types), ">")
html$text[grep("@description", html$text)] <- desc

transpile_write(html)
