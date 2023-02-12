from setuptools import setup, find_packages

VERSION = "0.0.1"
DESCRIPTION = "A performance monitor package"
LONG_DESCRIPTION = "A package that makes it easy to monitor process time"

setup(
    name="perfov",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author="Mert Cobanov",
    author_email="mertcobanov@gmail.com",
    license="MIT",
    packages=find_packages(),
    install_requires=[],
    keywords="timer",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
)
