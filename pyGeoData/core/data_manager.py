import json
from pathlib import Path
from typing import List, Optional
from pydantic import BaseModel
from pyGeoData.core.models.countries import Country
from pyGeoData.core.models.states import State
from pyGeoData.core.models.districts import District

class DataManager:
    _countries: List[Country] = []
    _states: List[State] = []
    _districts: List[District] = []
    _next_id = {"countries": 1, "states": 1, "districts": 1}

    @classmethod
    def load_data(cls):
        base_path = Path(__file__).parent / "data"
        try:
            with open(base_path / "countries.json", "r") as f:
                cls._countries = [Country(id=i+1, **data) for i, data in enumerate(json.load(f))]
                cls._next_id["countries"] = len(cls._countries) + 1
        except FileNotFoundError:
            pass

        try:
            with open(base_path / "states.json", "r") as f:
                cls._states = [State(id=i+1, **data) for i, data in enumerate(json.load(f))]
                cls._next_id["states"] = len(cls._states) + 1
        except FileNotFoundError:
            pass

        try:
            with open(base_path / "districts.json", "r") as f:
                cls._districts = [District(id=i+1, **data) for i, data in enumerate(json.load(f))]
                cls._next_id["districts"] = len(cls._districts) + 1
        except FileNotFoundError:
            pass

    @classmethod
    def get_countries(cls) -> List[Country]:
        return cls._countries

    @classmethod
    def get_states(cls) -> List[State]:
        return cls._states

    @classmethod
    def get_districts(cls) -> List[District]:
        return cls._districts

    @classmethod
    def create_country(cls, country: Country) -> Country:
        country.id = cls._next_id["countries"]
        cls._countries.append(country)
        cls._next_id["countries"] += 1
        return country

    @classmethod
    def create_state(cls, state: State) -> State:
        state.id = cls._next_id["states"]
        cls._states.append(state)
        cls._next_id["states"] += 1
        return state

    @classmethod
    def create_district(cls, district: District) -> District:
        district.id = cls._next_id["districts"]
        cls._districts.append(district)
        cls._next_id["districts"] += 1
        return district

    @classmethod
    def get_country(cls, country_id: int) -> Optional[Country]:
        return next((c for c in cls._countries if c.id == country_id), None)

    @classmethod
    def get_state(cls, state_id: int) -> Optional[State]:
        return next((s for s in cls._states if s.id == state_id), None)

    @classmethod
    def get_district(cls, district_id: int) -> Optional[District]:
        return next((d for d in cls._districts if d.id == district_id), None)

# Load data on module import
DataManager.load_data()
