# FontLab Python API Documentation - File Catalog

## Repository Overview

This repository contains the **FontLab 7 Python API documentation** - a comprehensive documentation system for FontLab 7's Python APIs, including typerig, fontgate, fontlab, FL, and PythonQt modules. The documentation is built using MkDocs and pydocmk2 to generate static HTML documentation from Python docstrings.

## Filesystem Tree

```
.
├── LICENSE
├── README.md
├── REVIEW/
├── docs/
├── fontlab7/
├── pythonqt/
```

## Root Level Files

### LICENSE
**Type**: Legal document  
**Purpose**: Apache License 2.0 - defines the legal terms for using and contributing to this documentation  
**Content**: Standard Apache 2.0 license text with copyright attribution to Fontlab Ltd.

### README.md
**Type**: Documentation  
**Purpose**: Main project documentation and build instructions  
**Content**: Explains how to view, build, and contribute to the FontLab 7 Python API documentation. Includes setup instructions for Python 2.7, pydocmk2, and mkdocs.

---

## Main Directories

### docs/
**Type**: Output directory  
**Purpose**: Generated static HTML documentation for public web hosting  
**Content**: Complete rendered documentation website hosted at fontlabcom.github.io

#### Core Documentation Files
- **index.html**: Main landing page for the documentation
- **404.html**: Custom 404 error page
- **sitemap.xml**: SEO sitemap for search engines
- **search/search_index.json**: Search index for documentation search functionality

#### API Documentation Structure
- **FL.*.html**: FontLab 5 legacy API documentation (Anchor, Canvas, Component, Dialog, etc.)
- **fontgate.*.html**: FontGate library API documentation (low-level font manipulation)
- **fontlab.*.html**: FontLab 7 native API documentation (high-level application interface)
- **typerig.*.html**: TypeRig library API documentation (community-developed utilities)

#### Static Assets
- **assets/**: Web assets for the documentation site
  - **fonts/**: Web fonts (FontAwesome, Material Icons)
  - **images/**: Icons and favicon
  - **javascripts/**: Site functionality (search, navigation, localization)
  - **stylesheets/**: CSS styling for the documentation theme

---

### fontlab7/
**Type**: Source directory  
**Purpose**: Main documentation build system for FontLab 7 APIs  

#### build/
**Purpose**: Build automation scripts  
- **build_fontlab7_api_docs.vfpy**: FontLab 7 script to generate markdown from Python docstrings
- **build_fontlab7_api_docs.command**: macOS shell script to build HTML documentation
- **build_fontlab7_api_docs.vfpyc**: Compiled version of the build script

#### Configuration Files
- **mkdocs.yml**: MkDocs configuration for HTML generation (theme, navigation, plugins)
- **pydocmk.yml**: pydocmk2 configuration for extracting Python docstrings and generating markdown

#### srcdocs/
**Purpose**: Source documentation and generated markdown files  

##### srcdocs/docs/
- **index.md**: Homepage content for the documentation

##### srcdocs/mkdocs/
**Purpose**: Auto-generated markdown files from Python docstrings  
**Content**: 300+ API reference files covering:
- **typerig.*.md**: TypeRig library modules (core utilities, GUI widgets, proxy objects)
- **fontgate.*.md**: FontGate library modules (font data structures, import/export options)
- **fontlab.*.md**: FontLab 7 native modules (UI components, tools, data objects)
- **FL.*.md**: Legacy FontLab 5 API compatibility layer

##### srcdocs/post/
**Purpose**: Post-processing markdown additions (appended to auto-generated docs)
- **fontlab.flWorkspace.md**: Additional documentation for workspace functionality

#### theme/
**Purpose**: Custom MkDocs theme files  
- **404.html**: Custom 404 page template
- **style/fontlab_pyapi.css**: Custom CSS styling for FontLab branding

---

### pythonqt/
**Type**: Source directory  
**Purpose**: Documentation build system for PythonQt API (Qt bindings for FontLab)

#### build/
- **build_pythonqt_api_docs.vfpy**: Build script for PythonQt documentation
- **build_pythonqt_api_docs.command**: macOS build automation

#### Configuration Files
- **mkdocs.yml**: MkDocs configuration for PythonQt docs (separate from main docs)
- **pydocmk.yml**: pydocmk2 configuration for PythonQt modules

#### srcdocs/
##### srcdocs/docs/
- **index.md**: PythonQt documentation homepage
- **PythonQt.QtCore.md**: Sample QtCore documentation

##### srcdocs/mkdocs/
**Purpose**: Generated PythonQt API documentation  
**Content**: Qt framework bindings including:
- **PythonQt.Qt.md**: Main Qt module
- **PythonQt.QtCore.md**: Core Qt functionality
- **PythonQt.QtGui.md**: GUI components
- **PythonQt.QtOpenGL.md**: OpenGL integration
- **PythonQt.QtSvg.md**: SVG support
- **PythonQt.QtUiTools.md**: UI development tools
- **PythonQt.QtXml.md**: XML parsing
- **PythonQt.QtXmlPatterns.md**: XML pattern matching
- **PythonQt.private.md**: Private Qt interfaces

#### theme/
- **style/fontlab_pyapi.css**: Consistent styling with main documentation

---

### REVIEW/
**Type**: Analysis directory (newly created)  
**Purpose**: Contains this file catalog and improvement recommendations  
**Content**: Documentation analysis and improvement proposals for the repository

---

## Key Technology Stack

### Documentation Generation
- **pydocmk2**: Python docstring extraction and markdown generation
- **MkDocs**: Static site generator with Material theme
- **Python 2.7**: Required runtime for FontLab 7 integration

### API Coverage
- **typerig**: Community-developed font manipulation utilities
- **fontgate**: Low-level font data access and manipulation
- **fontlab**: High-level FontLab 7 application interface
- **FL**: Legacy FontLab 5 compatibility layer
- **PythonQt**: Qt framework bindings for GUI development

### Web Technologies
- **Material Design theme**: Modern, responsive documentation interface
- **Search functionality**: Full-text search across all documentation
- **Responsive design**: Mobile and desktop compatibility
- **Syntax highlighting**: Code examples with proper highlighting

---

## File Organization Patterns

### Naming Conventions
- Module files follow Python package structure: `package.module.submodule.md`
- Generated files use consistent naming across all API libraries
- Build scripts use descriptive names indicating their purpose

### Directory Structure
- Clear separation between source (`srcdocs/`) and output (`docs/`)
- Parallel structure for fontlab7 and pythonqt documentation systems
- Dedicated build directories with automation scripts
- Theme customization isolated in separate directories

### Documentation Hierarchy
- Homepage and navigation structure defined in `mkdocs.yml`
- API documentation organized by library and module hierarchy
- Cross-references and linking maintained automatically
- Search indexing covers all documentation content