from distutils.core import setup
setup(
  name = 'charter',
  packages = ['charter'],
  version = '0.1',
  license='MIT',
  description = 'Chart-based Fact Checker & QA',
  author = 'Matthieu Moullec',
  author_email = 'matthieu.moullec.perso@gmail.com',
  url = 'https://github.com/matthieu-perso/charter',
  download_url = 'https://github.com/matthieu-perso/charter/archive/refs/tags/v0.1.tar.gz',
  keywords = ['Large Language Model', 'LLM', 'API', 'Fact-checking'],
  install_requires=[
          'requests',
          'json',
          'PIL'
          'transformers',
          'langchain'
      ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
  ],
)