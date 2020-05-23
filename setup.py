import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="smspva-wrapper",
    version="0.0.2",
    author="Terry",
    author_email="terry@beatwo.men",
    description="SMSPVA wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/h4n1virus/smspva-wrapper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: WTFPL License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
