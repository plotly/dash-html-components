from dash.development.component_loader import _get_metadata


def main():
    data = _get_metadata('dash_html_components/metadata.json')

    # Iterate over each property name (which is a path to the component)
    for componentPath in data:
        name = componentPath.split('/').pop().split('.')[0]
        with open('dash_html_components/{}.py'.format(name), 'r') as f:
            class_lines = f.read().split('\n')
        schema = eval(class_lines[6][9:])
        for key in schema.copy().keys():
            if key != 'children':
                schema.pop(key)
        with open('dash_html_components/{}.py'.format(name), 'w') as f:
            f.write('\n'.join(
                class_lines[:6] +
                ['schema = {}'.format(schema)] +
                class_lines[7:]
            ))

if __name__ == '__main__':
    main()
