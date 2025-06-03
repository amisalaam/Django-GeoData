from fastapi import APIRouter, HTTPException
from pyGeoData.core.data_manager import DataManager
from pyGeoData.core.models.countries import Country
from pyGeoData.core.schemas.countries import CountryCreate, Country
from typing import List

router = APIRouter()

@router.post("/countries/", response_model=Country)
def create_country(country: CountryCreate):
    new_country = Country(id=0, **country.dict())
    return DataManager.create_country(new_country)

@router.get("/countries/", response_model=List[Country])
def read_countries(skip: int = 0, limit: int = 100):
    countries = DataManager.get_countries()
    return countries[skip:skip + limit]

@router.get("/countries/{country_id}", response_model=Country)
def read_country(country_id: int):
    country = DataManager.get_country(country_id)
    if country is None:
        raise HTTPException(status_code=404, detail="Country not found")
    return country
