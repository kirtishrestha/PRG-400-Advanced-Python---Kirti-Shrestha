from setuptools import setup, find_packages

setup(
    name='prgPackages',  # Package name
    version='0.1',  # Version number
    description='A simple math package',  # Brief description
    long_description=open('README.md').read(),  # README as long description
    long_description_content_type='text/markdown',  # Markdown format for README
    author='Kirti Shrestha',
    author_email='pratisthashrestha2022@gmail.com',
    packages=find_packages(),  # Automatically find and include all packages
    classifiers=[  # Metadata to categorize the package
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Minimum Python version
)