from distutils.core import setup


setup(
    name='Django HTTP Proxy',
    version='0.1alpha1',
    description='A simple HTTP proxy for the Django framework.',
    author='Yuri van der Meer',
    author_email='python.org@yvandermeer.net',
    url='http://bitbucket.org/yvandermeer/django-http-proxy/',
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
        'Natural Language :: Dutch',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)