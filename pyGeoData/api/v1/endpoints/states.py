from fastapi import APIRouter, HTTPException
from pyGeoData.core.data_manager import DataManager
from pyGeoData.core.models.states import State
from pyGeoData.core.schemas.states import StateCreate, State
from typing import List

router = APIRouter()

@router.post("/states/", response_model=State)
def create_state(state: StateCreate):
    new_state = State(id=0, **state.dict())
    return DataManager.create_state(new_state)

@router.get("/states/", response_model=List[State])
def read_states(skip: int = 0, limit: int = 100):
    states = DataManager.get_states()
    return states[skip:skip + limit]

@router.get("/states/{state_id}", response_model=State)
def read_state(state_id: int):
    state = DataManager.get_state(state_id)
    if state is None:
        raise HTTPException(status_code=404, detail="State not found")
    return state
