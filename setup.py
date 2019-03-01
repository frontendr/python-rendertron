import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='rendertron',
    version='0.0.1',
    author='Johan Arensman',
    author_email='johan@frontendr.com',
    description='Rendertron middleware for python applications',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/frontendr/python-rendertron',
    packages=setuptools.find_packages(),
    classifiers=[
        'Framework :: Django',
        'Framework :: Django :: 2.1',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
