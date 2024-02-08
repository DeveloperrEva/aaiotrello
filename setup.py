from setuptools import setup
from textwrap import dedent

setup(name='aaiotrello',
      version='1',
      packages=['aaiotrello'],
      description='Async Python library for interacting with the Trello API',
      long_description=dedent("""\
        Python Trello API Wrapper
        --------------------------

        This Python API is simply a wrapper around the Trello API

        Getting Started:
        ----------------
        To use the Trello API, install the package either by downloading the source and running

          $ python setup.py install

        Documentation:
        --------------
        You can find documentation for the Python API at:

            http://packages.python.org/trello/

        And documentation for the Trello API at:

            https://trello.com/docs/api/

        """),
      url='https://trello.com/',
      download_url='https://github.com/developerreva/aaiotrello',
      install_requires=['requests>=0.9.1'],
      requires='requests',
      license='BSD License',
      classifiers=[
          "Development Status :: 1 - Beta",
              'Intended Audience :: Developers',
              'License :: OSI Approved :: BSD License',
              'Operating System :: OS Independent',
              'Programming Language :: Python',
              'Programming Language :: Python :: 3',
              'Programming Language :: Python :: 3.6',
      ],
      include_package_data=True,
      )
