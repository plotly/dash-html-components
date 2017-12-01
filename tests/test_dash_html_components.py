import dash_html_components
import unittest


class TestDashHtmlComponents(unittest.TestCase):
    def test_imports(self):
        with open('./scripts/data/elements.txt') as f:
            elements = map(
                lambda s: s[0].upper() + s[1:],
                f.read().split('\n')
            )
            elements += ['MapEl', 'ObjectEl', 'component']
            for s in ['Slot', 'Map', 'Object']:
                elements.remove(s)

        self.assertEqual(
            set([d for d in dir(dash_html_components) if d[0] != '_']),
            set(elements)
        )

    def test_sample_items(self):
        Div = dash_html_components.Div
        Img = dash_html_components.Img

        layout = Div(
            Div(
                Img(src='https://plot.ly/~chris/1638.png')
            ), style={'color': 'red'}
        )

        self.assertEqual(
            repr(layout),
            ''.join([
                "Div(children=Div(Img(src='https://plot.ly/~chris/1638.png')), "
                "style={'color': 'red'})"
            ])
        )

        self.assertEqual(
            layout._namespace, 'dash_html_components'
        )

    def test_to_html5(self):
        test_cases = [
            {
                'name': 'None Children',
                'input': html.Div(),
                'output': '<div></div>'
            },
            {
                'name': 'Text Children',
                'input': html.Script('alert'),
                'output': '<script>alert</script>'
            },
            {
                'name': 'Numerical Children',
                'input': html.Div(3),
                'output': '<div>3</div>'
            },
            {
                'name': 'Single Attribute',
                'input': html.Script('alert', type='text/javascript'),
                'output': '<script type="text/javascript">alert</script>'
            },
            {
                'name': 'Multiple Attributes',
                'input': html.A(href='codepen', target='_blank'),
                'output': '<a href="codepen" target="_blank"></a>'
            },
            {
                'name': 'Void Elements',
                'input': html.Link(rel='stylesheet', type='text/css'),
                'output': '<link rel="stylesheet" type="text/css">'
            },
            {
                'name': 'Style',
                'input': html.Div(style={'fontSize': '15px', 'color': 'blue'}),
                'output': '<div style="font-size: 15px; color: blue"></div>'
            },
            {
                'name': 'className',
                'input': html.Div(className='container'),
                'output': '<div class="container"></div>'
            },
            {
                'name': 'Nested Children',
                'input': html.Div([
                    3,
                    html.H1('header'),
                    html.Div(),
                    html.Div(
                        html.P([
                            html.Img(src='imgur', className='full-bleed')
                        ])
                    )
                ], className='parent'),
                'output': '\n'.join([
                    '<div class="parent">',
                    '3',
                    '<h1>header</h1>',
                    '<div></div>',
                    '<div>',
                    '<p>',
                    '<img src="imgur" class="full-bleed">'
                    '</p>',
                    '</div>',
                    '</div>'
                ])
            }
        ]
        for test_case in test_cases:
            self.assertEqual(
                test_case['input'].to_html5(),
                test_case['output']
            )
