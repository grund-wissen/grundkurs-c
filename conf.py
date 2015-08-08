# import sys, os
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.doctest',
              'sphinx.ext.intersphinx', 'sphinx.ext.todo',
              'sphinx.ext.coverage', 'sphinx.ext.pngmath',
              'sphinx.ext.ifconfig', 'sphinx.ext.viewcode']
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = 'Grundkurs C'
copyright = '2015, Bernhard Grotz'
version = '0.2.0'
release = '0.2.0'
# exclude_patterns = ["physik"]
language = 'de'
spelling_lang = 'de_DE'
exclude_patterns = []
pygments_style = 'sphinx'
html_theme = 'sphinxdoc'
html_static_path = ['_static']
html_additional_pages = {'home': 'home.html'}
htmlhelp_basename = 'Grundkurs C'
html_short_title = "Grundkurs C"

exclude_patterns = ["notes.rst", "*/notes.rst",
                    "**/notes.rst","todos.rst","README.rst"]

html_logo = "logo.png"
html_favicon = "favicon.ico"

html_last_updated_fmt = '%d. %b %Y'

html_use_smartypants = True
html_domain_indices  = False
html_use_index       = True
html_show_sourcelink = True
html_show_copyright  = False
html_show_sphinx     = False
html_search_language = 'en'
html_search_options = {'type': 'default'}

trim_footnote_reference_space = True

latex_preamble = r'''
\usepackage[version=3]{mhchem}
\usepackage{amsmath, units}
\usepackage{amsfonts, amssymb}
\usepackage{nicefrac,marvosym} 
\setcounter{secnumdepth}{-1}
\setlength{\headheight}{15pt}
\setcounter{tocdepth}{3}
'''

pngmath_latex_preamble = latex_preamble
latex_elements = {
    "preamble": latex_preamble,
    "babel": "\\usepackage[ngerman]{babel}",
    "classoptions": 'oneside,openany',
    "papersize": 'a4paper',
    "pointsize": '12pt',
    "fontpkg": '',
    "fncychap": '\\usepackage[Conny]{fncychap}'
}
# Glenn ist auch schick


latex_documents = [
  ('index', 'grundkurs-c.tex', 'Grundkurs C',
   'Bernhard Grotz', 'manual'),
]

intersphinx_mapping = {
    'gw': ('http://grund-wissen.de/', None),
    'gwe': ('http://grund-wissen.de/elektronik', None),
    'gwm': ('http://grund-wissen.de/mathematik', None),
    'gwp': ('http://grund-wissen.de/physik', None),
    'gwl': ('http://grund-wissen.de/linux', None),
    'gwip': ('http://grund-wissen.de/informatik/python', None),
    'gwil': ('http://grund-wissen.de/informatik/latex', None),
}

