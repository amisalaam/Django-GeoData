from fastapi import FastAPI
from pyGeoData.api.v1.endpoints import countries, states, districts

app = FastAPI(title="pyGeoData API", version="0.1.0")

# Include routers conditionally
app.include_router(countries.router, prefix="/v1", tags=["Countries"])
try:
    app.include_router(states.router, prefix="/v1", tags=["States"])
except AttributeError:
    pass
try:
    app.include_router(districts.router, prefix="/v1", tags=["Districts"])
except AttributeError:
    pass

@app.get("/")
async def root():
    return {"message": "Welcome to pyGeoData API"}
