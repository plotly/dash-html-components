from setuptools import setup

setup(
    name='dash_html_components',
    version='0.3.1',
    author='plotly',
    packages=['dash_html_components'],
    data_files=[('js', ['lib/bundle.js', 'lib/metadata.json'])],
    license='MIT',
    description='Dash UI component suite',
    install_requires=['flask', 'plotly', 'flask-cors', 'dash.ly']
)
