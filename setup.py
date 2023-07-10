from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in one_company/__init__.py
from one_company import __version__ as version

setup(
	name="one_company",
	version=version,
	description="An app where you will find rides for you and your family.",
	author="ali jafer",
	author_email="abbu050684@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
