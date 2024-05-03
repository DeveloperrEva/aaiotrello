from setuptools import setup
from textwrap import dedent

with open("README.md", "r", encoding="utf8") as fh:
    long_description = fh.read()

setup(name='aaiotrello',
      version='2.0.0',
      packages=['aaiotrello'],
      description='Async Python library for interacting with the Trello API',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://trello.com/',
      download_url='https://github.com/developerreva/aaiotrello',
      keywords='python python3 api-client aiohttp api-wrapper trello trello-api trello-async',
      install_requires=['aiohttp>=3.9.0'],
      requires='aiohttp',
      license='BSD License',
      author='Developereva',
      author_email='developereva@protonmail.com',
      project_urls={
        'Source Code': 'https://github.com/developerreva/aaiotrello',
        'Documentation': 'https://github.com/developerreva/aaiotrello#-getting-started',
        'Trello REST API Documentation': 'https://developer.atlassian.com/cloud/trello/rest/'
    },
      classifiers=[
	    	"Programming Language :: Python :: 3.7",
	    	"License :: OSI Approved :: MIT License",
	    	"Operating System :: OS Independent",
	    ],
      include_package_data=True,
      )
