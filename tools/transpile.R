if (!require(dashRtranspile)) remotes::install_github("plotly/dashRtranspile")

library(dashRtranspile)

html <- transpile(prefix = "html")

# add a link to the description section (currently no description is provided)
desc <- paste0("#' @description See <https://developer.mozilla.org/en-US/docs/Web/HTML/Element/", tolower(html$types), ">")
html$text[grep("@description", html$text)] <- desc

transpile_write(html)
