# -*- coding: utf-8 -*-
import os
from datetime import datetime


on_rtd = os.environ.get('READTHEDOCS', None) == 'True'


# -- General configuration -----------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
]

autodoc_member_order = 'bysource'

# Bootstrap Django for autodoc
import django
from django.conf import settings
settings.configure()
django.setup()

templates_path = ['_templates']

source_suffix = '.rst'

master_doc = 'index'

project = u'Django HTTP Proxy'
copyright = u'2009-{}, Yuri van der Meer'.format(datetime.today().year)

exclude_trees = ['_build']

pygments_style = 'sphinx'


# -- Options for HTML output ---------------------------------------------------

if not on_rtd: # only import and set the theme if we're building docs locally
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

    version = release = __import__('httpproxy').__version__
