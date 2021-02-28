from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

# Deploy to PyPI
#
# pip install twine wheel
# python setup.py sdist bdist_wheel
# twine upload --skip-existing dist/*

setup(
    name="stockai",
    version="1.5.0",
    author="Dale Nguyen",
    author_email="dale@dalenguyen.me",
    description="Get stock info from Yahoo! Finance",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dalenguyen/stockai",
    packages=find_packages(),
    install_requires = [ 'ciso8601', 'requests', 'loguru' ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
)
