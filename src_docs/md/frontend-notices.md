---
this_file: src_docs/md/frontend-notices.md
---
# Browser asset notices

These notices cover the named browser components below. The complete transitive
inventory is **still being reviewed**. This page does not qualify the site for
publication or change the licence of example code, API documentation or packages.

MaterialX supplies browser code, styles, search helpers and icons. The separate
FontLab shared theme includes Basecoat, daisyUI and Tailwind CSS. The Google Fonts
links request Roboto and Roboto Mono from an external service; those response
bytes can vary. The font notices below correspond to the reviewed response.

The [machine-readable notice list](frontend-notices.json) records source URLs,
full-text SHA-256 digests and remaining review items. MaterialX's dependency
versions are bound to publisher commit
[`c088af2`](https://github.com/jaywhj/mkdocs-materialx/tree/c088af2faa3a75dd4b9cded468eca285b6775d71).
Retained archive assets keep their existing bytes and attribution.

| Component | Version / source | Terms and full notices |
| --- | --- | --- |
| MaterialX | [10.1.5](https://pypi.org/project/mkdocs-materialx/10.1.5/) | MIT: [mit-materialx.txt](licenses/mit-materialx.txt) |
| Lunr | [2.3.9](https://registry.npmjs.org/lunr/-/lunr-2.3.9.tgz) | MIT: [source header notice](licenses/mit-lunr.txt); [npm distribution notice](licenses/mit-lunr-npm.txt) |
| clipboard | [2.0.11](https://registry.npmjs.org/clipboard/-/clipboard-2.0.11.tgz) | MIT: [mit-clipboard.txt](licenses/mit-clipboard.txt) |
| escape-html | [1.0.3](https://registry.npmjs.org/escape-html/-/escape-html-1.0.3.tgz) | MIT: [mit-escape-html.txt](licenses/mit-escape-html.txt) |
| focus-visible | [5.2.1](https://registry.npmjs.org/focus-visible/-/focus-visible-5.2.1.tgz) | W3C-20150513: [w3c-focus-visible.txt](licenses/w3c-focus-visible.txt) |
| rxjs | [7.8.2](https://registry.npmjs.org/rxjs/-/rxjs-7.8.2.tgz) | Apache-2.0: [apache-2.0-rxjs.txt](licenses/apache-2.0-rxjs.txt) |
| tslib | [2.7.0](https://registry.npmjs.org/tslib/-/tslib-2.7.0.tgz) | 0BSD: [0bsd-tslib.txt](licenses/0bsd-tslib.txt); [tslib-copyright.txt](licenses/tslib-copyright.txt) |
| material-design-color | [2.3.2](https://registry.npmjs.org/material-design-color/-/material-design-color-2.3.2.tgz) | MIT: [mit-material-design-color.txt](licenses/mit-material-design-color.txt) |
| tiny-emitter | [2.1.0](https://registry.npmjs.org/tiny-emitter/-/tiny-emitter-2.1.0.tgz) | MIT: [mit-tiny-emitter.txt](licenses/mit-tiny-emitter.txt) |
| lunr-languages | [1.14.0](https://registry.npmjs.org/lunr-languages/-/lunr-languages-1.14.0.tgz) | MPL-1.1 (package; embedded components retain their terms): [mpl-1.1-lunr-languages.txt](licenses/mpl-1.1-lunr-languages.txt) |
| basecoat-css | [1.0.2](https://i.fontlab.com/fltheme26/1.0.0/licenses/basecoat-css.txt) | MIT: [mit-basecoat-css.txt](licenses/mit-basecoat-css.txt) |
| daisyui | [5.7.44](https://i.fontlab.com/fltheme26/1.0.0/licenses/daisyui.txt) | MIT: [mit-daisyui.txt](licenses/mit-daisyui.txt) |
| tailwindcss | [4.3.3](https://i.fontlab.com/fltheme26/1.0.0/licenses/tailwindcss.txt) | MIT: [mit-tailwindcss.txt](licenses/mit-tailwindcss.txt) |
| FontLab shared theme | [fltheme26/1.0.0 (response snapshot)](https://i.fontlab.com/fltheme26/) | Apache-2.0: [apache-2.0.txt](licenses/apache-2.0.txt) |
| @mdi/svg | [7.4.47](https://registry.npmjs.org/@mdi/svg/-/svg-7.4.47.tgz) | Apache-2.0 (icons); MIT (code): [pictogrammers-free.txt](licenses/pictogrammers-free.txt) |
| @fortawesome/fontawesome-free | [7.1.0](https://registry.npmjs.org/@fortawesome/fontawesome-free/-/fontawesome-free-7.1.0.tgz) | CC-BY-4.0 (SVG icons): [fontawesome-free.txt](licenses/fontawesome-free.txt) |
| Creative Commons Attribution | [4.0](https://raw.githubusercontent.com/spdx/license-list-data/main/text/CC-BY-4.0.txt) | CC-BY-4.0: [cc-by-4.0.txt](licenses/cc-by-4.0.txt) |
| @primer/octicons | [19.25.0](https://registry.npmjs.org/@primer/octicons/-/octicons-19.25.0.tgz) | MIT: [mit-octicons.txt](licenses/mit-octicons.txt) |
| lucide-static | [1.11.0](https://registry.npmjs.org/lucide-static/-/lucide-static-1.11.0.tgz) | ISC: [isc-lucide.txt](licenses/isc-lucide.txt) |
| Roboto | [external Google Fonts response snapshot](https://raw.githubusercontent.com/google/fonts/2e69e0bf1bd2662d6775bb54a398bded758e87cf/ofl/roboto/OFL.txt) | OFL-1.1: [ofl-roboto.txt](licenses/ofl-roboto.txt) |
| Roboto Mono | [external Google Fonts response snapshot](https://raw.githubusercontent.com/google/fonts/b01086459d9d41ece904d39155b93f7bd3a676f2/ofl/robotomono/OFL.txt) | OFL-1.1: [ofl-robotomono.txt](licenses/ofl-robotomono.txt) |
| UMD contributors | [returnExports wrapper](https://github.com/umdjs/umd/blob/master/LICENSE.md) | MIT: [mit-umd.txt](licenses/mit-umd.txt) |
| mkdocstrings-python frontend CSS | [2.0.9](https://pypi.org/project/mkdocstrings-python/2.0.9/) | ISC: [isc-mkdocstrings-python.txt](licenses/isc-mkdocstrings-python.txt) |

## Review still open

- Complete provenance and source availability for the 29 modules and dictionary in wordcut.js; its upstream Wordcut source is LGPL-3.0.
- TinySegmenter original BSD full notice and exact wrapper/source provenance.
- Clipboard nested delegate/good-listener/select notices and embedded-version closure.
- CSS data-SVG components and any historical archive-only frontend dependencies.
- External-font response variants, complete shared-theme build provenance, and full site publication gates.

The supplied lunr-languages source distribution is linked above. Embedded
components keep their own licences; its package licence is not a blanket
licence for every bundled library or dictionary.

The Lunr browser source header carries a 2020 copyright; its npm archive
retains a 2013 licence notice. Both are preserved above.

This API site also retains its existing Lunr TokenSet separator fix. The
[patch source](https://github.com/fontlabcom/fontlab-python-docs/blob/d5dfd0e7bf0ac90ac84d6b8b8e943dc93301e823/scripts/lunr_patch.py)
and the build bundle manifest record that modification. Source maps retain
the original upstream text.
