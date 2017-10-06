# dashHtmlComponents

Vanilla HTML components for Dash

## Installation

dashHtmlComponents is not yet available on CRAN, but you can install with:

```r
remotes::install_github("plotly/dash-html-components")
```

## Usage

```r
library(dashHtmlComponents)
library(dasher)

app <- Dash$new()

app$layout_set(
  exampleComponent(id = "inputID", value = "initial value"),
  html_div(id = "outputID")
)

app$callback(
  function(x = input("inputID")) {
    sprintf("You've entered: '%s'", x)
  },
  output("outputID")
)

app$run_server(showcase = TRUE)
```
