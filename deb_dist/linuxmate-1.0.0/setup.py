from setuptools import setup
with open("README.md","r",encoding="utf-8") as readme_file:
	long_description = readme_file.read()

setup(
	name="linuxmate",
	version="1.0.0",
	description="Answers all your questions related to Linux",
	long_description=long_description,
	long_description_content_type="text/markdown",
	author="BCodes",
	author_email="bcodes2350@gmail.com",
	license="GNU GPLv3",
	packages=['linuxmate'],
	package_dir={'linuxmate':'linuxmate/'},
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
		"Environment :: Console",
		"Operating System :: POSIX :: Linux",
	],
	entry_points={
		'console_scripts':['linuxmate = linuxmate.linuxmate:main']
	},
	keywords="Linux Questions Helper",
	python_requires=">=3.10"
)
