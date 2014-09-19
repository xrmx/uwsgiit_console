from setuptools import setup, find_packages
import os
import console

setup(
    name='uwsgiit-console',
    version=console.__version__,
    description='A django app to simplify the use of uWSGI.it API',
    long_description=open(
        os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    classifiers=[
        "Development Status :: Beta",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: JavaScript",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='uwsgit.it,console',
    author='20tab S.r.l.',
    author_email='info@20tab.com',
    url='https://github.com/20tab/uwsgiit_console',
    license='MIT License',
    platforms=['OS Independent'],
    install_requires=[
        'Django',
        'twentytab-select2',
        'uwsgiit-py>=0.8.1'
    ],
    packages=find_packages(exclude=['demo', 'demo.*']),
    include_package_data=True,
    package_data={
        '': ['*.html', '*.css', '*.js', '*.gif', '*.png', ],
    }
)