import os
from distutils.core import setup
here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()

setup(
    name='print_json_middleware',
    version='0.1',
    py_modules=['print_json_middleware'],
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
)
