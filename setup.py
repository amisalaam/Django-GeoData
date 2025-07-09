from setuptools import setup, find_packages

setup(
    name="django-geodata",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django>=3.2',
    ],
    package_data={
        'src': ['data/*.json'],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="A Django library for managing countries, states, and districts with foreign key relationships",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/amisalaam/Django-GeoData.git",
    classifiers=[
        "Framework :: Django",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)