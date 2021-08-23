import io
from setuptools import setup

setup(
    name="dash_html_components",
    version="2.0.0rc1",
    author="Chris Parmer <chris@plotly.com>",
    author_email="chris@plotly.com",
    packages=["dash_html_components"],
    url="https://github.com/plotly/dash-html-components",
    include_package_data=True,
    license="MIT",
    description="Vanilla HTML components for Dash",
    long_description=io.open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    install_requires=[],
)
