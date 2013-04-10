from setuptools import setup, find_packages
import polymorphic

setup(
    name = 'django_polymorphic',
    version = polymorphic.__version__,
    description = 'Seamless Polymorphic Inheritance for Django Models',
    url = 'https://github.com/chrisglass/django_polymorphic',

    author = 'Bert Constantin',
    author_email = 'bert.constantin@gmx.de',

    maintainer = 'Christopher Glass',
    maintainer_email = 'tribaal@gmail.com',

    packages = find_packages(),
    package_data = {
        'polymorphic': [
            'templates/admin/polymorphic/*.html',
        ],
    },

    install_requires=['setuptools'],
    test_suite='runtests',

    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
