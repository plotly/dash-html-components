import unittest
import dash_html_components


class TestDashHtmlComponents(unittest.TestCase):
    def test_imports(self):
        with open('./scripts/data/elements.txt') as f:
            elements = map(
                lambda s: s[0].upper() + s[1:],
                f.read().split('\n')
            )
            elements += ['MapEl', 'ObjectEl', 'component', 'version']
            for s in ['Map', 'Object']:
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
