from setuptools import setup

setup(
    name='dash_html_components',
    version='0.1.0',
    author='plotly',
    packages=['dash', 'dash/development'],
    license='MIT',
    description='Dash UI component suite',
    install_requires=['flask', 'plotly', 'flask-cors', 'dash.ly']
)
