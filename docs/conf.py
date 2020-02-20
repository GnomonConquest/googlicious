import sys
import os

sys.path.insert(0, os.path.abspath('../'))
exclude_dirnames = ["test"]
extensions = [
    'sphinx.ext.autodoc',
]

templates_path = ['_templates']

source_suffix = '.rst'

master_doc = 'index'

project = u'Googlicious'
copyright = u''
author = u'Dimitry Dukhovny'

version = u'0.1'
release = u'0.1'

language = None

exclude_patterns = ['_build',
                    '*/test/*',
                    'test/*',
                    '*/test',
                    '../*/test']

pygments_style = 'sphinx'

todo_include_todos = False

html_theme = 'sphinx_rtd_theme'

#html_theme_options = {}

#html_theme_path = []

#html_title = None

#html_short_title = None

#html_logo = None

#html_favicon = None

html_static_path = ['_static']

#html_extra_path = []

#html_last_updated_fmt = '%b %d, %Y'

#html_use_smartypants = True

#html_sidebars = {}

#html_additional_pages = {}

#html_domain_indices = True

#html_use_index = True

#html_split_index = False

#html_show_sourcelink = True

#html_show_sphinx = True

#html_show_copyright = True

#html_use_opensearch = ''

#html_file_suffix = None

#html_search_language = 'en'

#html_search_options = {'type': 'default'}

#html_search_scorer = 'scorer.js'

htmlhelp_basename = 'googlicious'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',

# Latex figure (float) alignment
#'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'googlicious.tex', u'Googlicious Documentation',
     u'Dimitry Dukhovny', 'manual'),
]

#latex_logo = None

#latex_use_parts = False

#latex_show_pagerefs = False

#latex_show_urls = False

#latex_appendices = []

#latex_domain_indices = True

man_pages = [
    (master_doc, 'googlicious', u'Googlicious Documentation',
     [author], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'Googlicious', u'Googlicious Documentation',
     author, 'Googlicious', 'Do security-related things with Google.',
     'Miscellaneous'),
]

#texinfo_appendices = []

#texinfo_domain_indices = True

#texinfo_show_urls = 'footnote'

#texinfo_no_detailmenu = False
