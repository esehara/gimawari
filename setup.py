try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup


setup(name='gimawari',
	  version="0.0.1",
	  packages=['gimawari'],
	  entry_points="""# -*- Entry Points: -*-
[console_scripts]
gimawari = gimawari.console:begin
	  """
	  )
