import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

# Deploy to PyPI
#
# pip install twine
# python setup.py sdist bdist_wheel
# twine upload --skip-existing dist/*

setuptools.setup(
    name="stockai",
    version="1.0.0",
    author="Dale Nguyen",
    author_email="dungnq@itbox4vn.com",
    description="Get stock info from Yahoo! Finance",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dalenguyen/stockai",
    packages=setuptools.find_packages(),
    install_requires = [ 'ciso8601', 'requests', 'loguru' ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
)
