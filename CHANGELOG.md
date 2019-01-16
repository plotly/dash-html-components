# Change Log for dash-html-components
All notable changes to this project will be documented in this file.
This project adheres to [Semantic Versioning](http://semver.org/).

## [0.13.2] - 2018-09-21
### Fixed
- Fixes Python3.7 incompatibility with `0.13.0` and `0.13.1`.

### Changed
- Regenerated classes with Python3.7 to remove `async` keyword.

## [0.13.1] - 2018-09-20
### Fixed
- Renamed `__init__.py` external_path to dash_html_components.min.js

## [0.13.0] - 2018-09-20
### Added
- Unminified dev bundle support. [#64](https://github.com/plotly/dash-html-components/pull/64)

## Unreleased

## [0.12.0] - 2018-06-01
### Changed
- `dash_html_components/__init__.py` now imports from python class files rather than generating classes at runtime,
adding support for IDE auto complete etc.

## [0.11.0] - 2018-06-01
### Added
- A `n_clicks_timestamp` property was added to all of the components. This property represents the date that the element was clicked on and can be used to determine _which element was clicked on_ in callbacks with multiple elements. This is considered a stop-gap solution: ultimately we'll want a solution that works for _all_ properties across all components, not just the `n_clicks` property. https://github.com/plotly/dash-html-components/pull/45

## [0.10.1] - 2018-04-29
### Added
- `aria-*` and `data-*` attributes are now supported in all dash html components [#40](https://github.com/plotly/dash-html-components/pull/40)
    These new keywords can be added using a dictionary expansion, e.g.
    ```
    html.Div(id="my-div", **{"data-toggle": "toggled", "aria-toggled": "true"})
    ```
- The `role` attribute was added to all components
- The `autoComplete` property was added to `textarea`

## [0.10.0] - 2018-04-03
### Added
- Previously, if a user named their app file `dash.py`, an unhelpful error
message would be raised. Now, `import dash_html_components` will check if
the user has a file named `dash.py` and warn the users appropriately.
https://github.com/plotly/dash-html-components/pull/39

## [0.9.0] - 2018-02-11
### Changed
- Moved `PropTypes` import from using `react` to using `prop-types` package to support using React 16+ in `dash-renderer`

### Added
- Added `Picture` and `Base` components
- Added `muted` property to `Audio` component

## [0.8.0] - 2017-09-29
### Added
- A `key` property has been added to every component. See https://reactjs.org/docs/lists-and-keys.html for more about this attribute.

## [0.7.0] - 2017-07-18
### Added
- A `n_clicks` property has been added to every component that gets incremented automatically when the element has been clicked on

## [0.2.3] - 2016-07-20
### Fixed
- `style` propType is now correctly set to object, not string

## [0.2.2] - 2016-07-17
### Fixed
- Issue with component metadata path in pypi package

## [0.2.0] - 2016-07-07
### Added
- Fix issues with attribute casing

## 0.1.0 - 2016-06-28
- Initial release

[0.2.3]: https://github.com/plotly/dash-html-components/compare/v0.2.2...v0.2.3
[0.2.2]: https://github.com/plotly/dash-html-components/compare/v0.2.0...v0.2.2
[0.2.0]: https://github.com/plotly/dash-html-components/compare/v0.1.0...v0.2.0
