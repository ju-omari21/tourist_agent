from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in tourist_agent/__init__.py
from tourist_agent import __version__ as version

setup(
	name="tourist_agent",
	version=version,
	description="This app is for a tourist agent system",
	author="Jullunar Alomari",
	author_email="Jullunar@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
