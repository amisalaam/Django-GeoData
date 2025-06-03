# pyGeoData

A modular Python package for geographic data (countries, states, districts) with FastAPI support. No database required!

## Installation

`ash
pip install pyGeoData
pip install pyGeoData[all]  # For all features
`

## Usage

### Run the API
`ash
uvicorn pyGeoData.main:app --reload
`

### API Endpoints
- GET /v1/countries/: List all countries
- POST /v1/countries/: Create a country
- GET /v1/states/: List all states
- POST /v1/states/: Create a state
- GET /v1/districts/: List all districts
- POST /v1/districts/: Create a district

### Direct Data Access
`python
from pyGeoData.core.data_manager import get_countries

countries = get_countries()
print([country.name for country in countries])
`

## Modular Installation
- Countries only: pip install pyGeoData[countries]
- Countries and states: pip install pyGeoData[states]
- All features: pip install pyGeoData[all]

## Contributing
Contributions are welcome! Please read the [contributing guidelines](CONTRIBUTING.md).

## License
MIT License
