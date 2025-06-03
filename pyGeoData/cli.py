import typer
from pyGeoData.core.data_manager import DataManager

app = typer.Typer()

@app.command()
def list_countries():
    """List all countries."""
    countries = DataManager.get_countries()
    for country in countries:
        typer.echo(f"ID: {country.id}, Name: {country.name}, Code: {country.code}")

@app.command()
def list_states():
    """List all states."""
    states = DataManager.get_states()
    for state in states:
        typer.echo(f"ID: {state.id}, Name: {state.name}, Country ID: {state.country_id}")

@app.command()
def list_districts():
    """List all districts."""
    districts = DataManager.get_districts()
    for district in districts:
        typer.echo(f"ID: {district.id}, Name: {district.name}, State ID: {district.state_id}")

if __name__ == "__main__":
    app()
