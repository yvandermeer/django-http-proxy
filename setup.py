import os.path
from distutils.core import setup

from httpproxy import __version__

here = os.path.dirname(os.path.abspath(__file__))

# Get long_description from index.txt
f = open(os.path.join(here, 'docs', 'index.txt'))
long_description = f.read().strip()
long_description = long_description.split('split here', 1)[1]
f.close()

setup(
    name='django-http-proxy',
    version=__version__,
    description='A simple HTTP proxy for the Django framework.',
    long_description=long_description,
    author='Yuri van der Meer',
    author_email='django-http-proxy@yvandermeer.net',
    url='http://httpproxy.yvandermeer.net/',
    download_url='http://bitbucket.org/yvandermeer/django-http-proxy/get/v%s.zip' % __version__,
    packages=[
        'httpproxy',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)