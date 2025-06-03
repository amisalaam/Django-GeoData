from fastapi import APIRouter, HTTPException
from pyGeoData.core.data_manager import DataManager
from pyGeoData.core.models.districts import District
from pyGeoData.core.schemas.districts import DistrictCreate, District
from typing import List

router = APIRouter()

@router.post("/districts/", response_model=District)
def create_district(district: DistrictCreate):
    new_district = District(id=0, **district.dict())
    return DataManager.create_district(new_district)

@router.get("/districts/", response_model=List[District])
def read_districts(skip: int = 0, limit: int = 100):
    districts = DataManager.get_districts()
    return districts[skip:skip + limit]

@router.get("/districts/{district_id}", response_model=District)
def read_district(district_id: int):
    district = DataManager.get_district(district_id)
    if district is None:
        raise HTTPException(status_code=404, detail="District not found")
    return district
