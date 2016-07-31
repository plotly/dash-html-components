from setuptools import setup

setup(
    name='dash_html_components',
    version='0.2.3',
    author='plotly',
    packages=['dash_html_components', 'lib'],
    package_data={'lib': ['../lib/*']},
    license='MIT',
    description='Dash UI component suite',
    install_requires=['flask', 'plotly', 'flask-cors', 'dash.ly']
)
