import os
import dash as _dash
import sys as _sys

current_path = os.path.dirname(os.path.abspath(__file__))

supported_react_attributes = [
    'id', 'style',

    'src', 'height', 'width', 'accept',
    'acceptCharset', 'accessKey', 'action', 'allowFullScreen',
    'allowTransparency', 'alt', 'async', 'autoComplete', 'autoFocus',
    'autoPlay', 'cellPadding', 'cellSpacing', 'charSet', 'checked',
    'classID', 'colSpan', 'cols', 'contentEditable',
    'contextMenu', 'controls', 'coords', 'crossOrigin', 'data',
    'dateTime', 'defer', 'dir', 'disabled', 'download', 'draggable',
    'encType', 'form', 'formAction', 'formEncType', 'formMethod',
    'formNoValidate', 'formTarget', 'frameBorder', 'headers', 'hidden',
    'high', 'href', 'hrefLang', 'htmlFor', 'httpEquiv', 'icon',
    'lang', 'list', 'loop', 'low', 'manifest', 'marginHeight',
    'marginWidth', 'max', 'maxLength', 'media', 'mediaGroup',
    'method', 'min', 'multiple', 'muted', 'name', 'noValidate',
    'open', 'optimum', 'pattern', 'placeholder', 'poster', 'preload',
    'radioGroup', 'readOnly', 'rel', 'required', 'role', 'rowSpan',
    'rows', 'sandbox', 'scope', 'scoped', 'scrolling', 'seamless',
    'selected', 'shape', 'size', 'sizes', 'span', 'spellCheck',
    'srcDoc', 'srcSet', 'start', 'step', 'tabIndex', 'target',
    'title', 'type', 'useMap', 'value', 'wmode']

_dash.development.component_loader.load_components(
    os.path.join(current_path, '../lib/metadata.json'),
    supported_react_attributes,
    globals(),
    _sys._getframe(1).f_globals.get('__name__', '__main__')
)
