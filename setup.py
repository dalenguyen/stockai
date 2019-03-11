import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="stockai",
    version="0.0.1",
    author="Dale Nguyen",
    author_email="dungnq@itbox4vn.com",
    description="Stock price prediction",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dalenguyen/stockai",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
)