# Contributing to dash-html-components

## Getting Started

Refer to the [readme](README.md) for installation and development workflow instructions.

## Contributions

[Dash HTML Components][] consist of generic HTML5 elements based on the [MDN spec][] <sup id="n1">[1](#f1)</sup>. For more complex UI components, see the [Dash Core Components][]. Contributions are welcome! This repository's open [Issues][] are a good place to start.

## Pull Request Guidelines

Using the [GitHub flow][] is encouraged when proposing contributions to this repository (i.e. creating a feature branch and submitting a PR on the master branch).

## Coding Style

Please lint any additions to react components with `npm run lint`. Rules defined in [.eslint](.eslint) are inherited from [`dash-components-archetype`](https://github.com/plotly/dash-components-archetype)'s [eslintrc-react.json](https://github.com/plotly/dash-components-archetype)

## Publishing New Features

For substantial new features (i.e. more than bug fixes and minor changes), the following steps are highly encouraged:

1. Create a pull request and tag the Plotly team `@plotly/dash` as well as an appropriate reviewer (frequent [contributors][] are a safe bet).
2. After a review has been done and your changes have been approved, create a prerelease and comment in the PR. Version numbers should follow [semantic versioning][] To create a prerelease:
    * Add `rc1` to `version.py` (`./dash_html_components/version.py`) e.g. `0.13.0rc1`
    * Add `-rc1` to `package.json` e.g. `0.13.0-rc1`
    * Update the `unpkg` link in `./dash_html_components/__init__.py`, replacing `__version__` with your release candidate (e.g. `"0.13.0-rc1"`)
    * Run `npm run publish-all`
3. Comment in the PR with the prerelease version
4. Update the top-level comment to include info about how to install, a summary of the changes, and a simple example. For a good example, see the [Confirmation Modal component][].
    * This makes it easier for a community member to come in and try it out. As more folks review, it's harder to find the installation instructions deep in the PR
    * Keep this top-level comment updated with installation instructions (e.g. the `pip install` command)
5. Make a post in the [Dash Community Forum][]
    * Title it `":mega: Announcement! New <Your Feature> - Feedback Welcome"`
    * In the description, link to the PR and any relevant issue(s)
    * Pin the topic so that it appears at the top of the forum for two weeks
    * For a good example, see the [Confirmation Modal announcement][]

[Dash HTML Components]: https://dash.plot.ly/dash-html-components
[MDN spec]: https://developer.mozilla.org/en-US/docs/Web/HTML/Element 
[Dash Core Components]: https://github.com/plotly/dash-core-components
[Issues]: https://github.com/plotly/dash-html-components/issues
[GitHub flow]: https://guides.github.com/introduction/flow/
[contributors]: https://github.com/plotly/dash-html-components/graphs/contributors
[eslintrc-react.json]: https://github.com/plotly/dash-components-archetype/blob/master/config/eslint/eslintrc-react.json
[semantic versioning]: https://semver.org/
[Dash Community Forum]: https://community.plot.ly/c/dash
[Confirmation Modal component]: https://github.com/plotly/dash-core-components/pull/211#issue-195280462
[Confirmation Modal announcement]: https://community.plot.ly/t/announcing-dash-confirmation-modal-feedback-welcome/11627

<b id="f1">1</b> Also see the [W3 index of elements](https://dev.w3.org/html5/html-author/#index-of-elements) [↩](#n1)

