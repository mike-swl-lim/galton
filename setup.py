from setuptools import setup, find_packages

setup(
    name = "galton",
    version = "0.0.2",
    author = "Michael Lim",
    author_email = "mikelimcontact1000@gmail.com",
    description = "Machine learning engineer challenge for endeavour group",
    url = "https://github.com/mike-swl-lim/ml-engineering-challenge",
    python_requires = ">=3.6*",
    packages = find_packages(include=('galton',)),
    install_requires = [
        "numpy",
        "sklearn",
        "matplotlib",
        "flask"
    ]
)