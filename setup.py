from distutils.core import setup


setup(
    name='django-http-proxy',
    version='0.1',
    description='A simple HTTP proxy for the Django framework.',
    author='Yuri van der Meer',
    author_email='python.org@yvandermeer.net',
    url='http://bitbucket.org/yvandermeer/django-http-proxy/',
    download_url='http://bitbucket.org/yvandermeer/django-http-proxy/get/v0.1.zip',
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