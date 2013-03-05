import os
from setuptools import setup, find_packages
here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()

setup(
    name='print_json_middleware',
    version='0.1.1',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    author='Sam Brauer',
    author_email='sam.brauer@gmail.com',
    url='https://github.com/sbrauer/print_json_middleware',
    license='MIT',
    description='JSON prettyprinter WSGI middleware',
    long_description=README,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Middleware",
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
    ],
    entry_points="""
        [paste.filter_app_factory]
        print_json = print_json_middleware:filter_app_factory
        [paste.filter_factory]
        print_json = print_json_middleware:filter_factory
    """,
)
