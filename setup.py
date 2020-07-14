import setuptools
from rendertron import version

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rendertron",
    version=version,
    author="Johan Arensman",
    author_email="johan@frontendr.com",
    description="Rendertron middleware for python applications",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/frontendr/python-rendertron",
    packages=setuptools.find_packages(include=["rendertron.*"]),
    classifiers=[
        "Development Status :: 4 - Beta",
        # 'Development Status :: 5 - Production/Stable',
        "Framework :: Django",
        "Framework :: Django :: 2.1",
        "Framework :: Django :: 3.0",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords="rendertron render chrome django middleware",
    python_requires=">=3",
)
