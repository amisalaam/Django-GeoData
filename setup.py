from setuptools import setup, find_packages

setup(
    name="pyGeoData",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "fastapi>=0.103.0",
        "uvicorn>=0.23.0",
        "pydantic>=2.0.0",
    ],
    extras_require={
        "countries": [],
        "states": ["pyGeoData[countries]"],
        "districts": ["pyGeoData[states]"],
        "all": ["pyGeoData[countries,states,districts]"],
    },
    include_package_data=True,
    package_data={
        "pyGeoData": ["core/data/*.json"],
    },
    entry_points={
        "console_scripts": [
            "pygeodata = pyGeoData.cli:app",
        ],
    },
)
