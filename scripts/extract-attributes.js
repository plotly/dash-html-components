'use strict';

const fs = require('fs');
const cheerio = require('cheerio');
const request = require('request');
const S = require('string');

const htmlURL = 'https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes';
const dataPath = './data/attributes.json';

// From https://facebook.github.io/react/docs/tags-and-attributes.html#supported-attributes
// less the `data` attribute,
// the special `className` and `htmlFor` props,
// and `httpEquiv` + `acceptCharset` which are already correctly camelCased.
const supportedAttributes = ['accept', 'accessKey', 'action',
'allowFullScreen', 'allowTransparency', 'alt', 'async', 'autoComplete',
'autoFocus', 'autoPlay', 'capture', 'cellPadding', 'cellSpacing', 'challenge',
'charSet', 'checked', 'cite', 'classID', 'colSpan', 'cols', 'content',
'contentEditable', 'contextMenu', 'controls', 'coords', 'crossOrigin',
'dateTime', 'default', 'defer', 'dir', 'disabled', 'download', 'draggable',
'encType', 'form', 'formAction', 'formEncType', 'formMethod', 'formNoValidate',
'formTarget', 'frameBorder', 'headers', 'height', 'hidden', 'high', 'href',
'hrefLang', 'icon', 'id', 'inputMode', 'integrity', 'is',
'keyParams', 'keyType', 'kind', 'label', 'lang', 'list', 'loop', 'low',
'manifest', 'marginHeight', 'marginWidth', 'max', 'maxLength', 'media',
'mediaGroup', 'method', 'min', 'minLength', 'multiple', 'muted', 'name',
'noValidate', 'nonce', 'open', 'optimum', 'pattern', 'placeholder', 'poster',
'preload', 'profile', 'radioGroup', 'readOnly', 'rel', 'required', 'reversed',
'role', 'rowSpan', 'rows', 'sandbox', 'scope', 'scoped', 'scrolling',
'seamless', 'selected', 'shape', 'size', 'sizes', 'span', 'spellCheck', 'src',
'srcDoc', 'srcLang', 'srcSet', 'start', 'step', 'style', 'summary', 'tabIndex',
'target', 'title', 'type', 'useMap', 'value', 'width', 'wmode', 'wrap'];

// Create a map of HTML attribute to React prop
// e.g. {"datetime": "dateTime"}
const attributeMap = supportedAttributes.reduce((map, reactAttribute) => {
    const htmlAttribute = reactAttribute.toLowerCase();
    map[htmlAttribute] = reactAttribute;

    return map;
},
    // Start the map with two attributes that have special names in React, and
    // two attributes that already have camelCasing in HTML.
    {
        'class': 'className',
        'for': 'htmlFor',
        'httpEquiv': 'httpEquiv',
        'acceptCharset': 'acceptCharset'
    }
);

/**
 * From the MDN attributes reference, extract a map of attributes with
 * descriptions and supported elements.
 */
function extractAttributes($) {
    const $table = $('#Attribute_list').next('table');
    const attributes = {};

    $table.find('tbody tr').each((i, row) => {
        const $children = cheerio(row).find('td');
        const attribute = $children.eq(0).text();

        const elements = $children.eq(1).text()
            .replace(/[<>\s]/g, '')
            .split(',');

        const description = $children.eq(2).text()
            .replace(/\n/g, '')
            // Fix irregular whitespace characters
            .replace(' ', ' ')
            .trim();

        const htmlAttribute = S(attribute)
            .trim()
            // Convert e.g. `accept-charset` to `acceptCharset`
            .camelize()
            .toString();

        // Skip `data-*` attributes
        if (htmlAttribute.indexOf('data') === 0) {
            return true;
        }

        // Ensure attribute is supported by React
        if (!attributeMap[htmlAttribute]) {
            return true;
        }

        // maxlength -> maxLength; class -> className
        const reactAttribute = attributeMap[htmlAttribute];

        attributes[reactAttribute] = {
            elements,
            description
        };

    });

    return attributes;
}

/**
 * Create a map of elements to attributes e.g. {div: ['id', 'name']}
 */
function extractElements(attributes) {
    return Object.keys(attributes)
        .reduce((elementMap, attributeName) => {
            const attribute = attributes[attributeName];
            const elements = attribute.elements;

            elements.forEach((element) => {
                elementMap[element] = elementMap[element] || [];
                elementMap[element].push(attributeName);
            });

            return elementMap;
        }, {});
}

// A local copy of the MDN attributes web page has been saved for reference:
// fs.readFile('./data/attributes.html', 'utf-8', (error, html) => {
request(htmlURL, (error, response, html) => {
    if (error) {
        throw error;
    }
    const $ = cheerio.load(html);
    const attributes = extractAttributes($);
    const elements = extractElements(attributes);
    const out = {
        attributes,
        elements
    };

    // Print out JSON with 4-space indentation formatting.
    // http://stackoverflow.com/a/11276104
    fs.writeFileSync(dataPath, JSON.stringify(out, null, 4));
});
