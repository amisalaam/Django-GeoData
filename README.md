Django Geo Regions
A Django library for managing countries, states, and districts with foreign key relationships.
Installation
Install the library using pip:
pip install django-geo-regions

Setup

Add django_geo_regions to your INSTALLED_APPS in your Django settings:

INSTALLED_APPS = [
    ...
    'django_geodata',
]


Run migrations to create the tables and populate initial data:

python manage.py makemigrations
python manage.py migrate

Usage
You can use the models in your Django project:
from django_geo_regions.models import Country, State, District

# Example: Create a new model with a foreign key to District
class MyModel(models.Model):
    name = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='mymodels')

# Querying examples
countries = Country.objects.all()
states = State.objects.filter(country__code='USA')
districts = District.objects.filter(state__name='California')

Models

Country: Represents a country with a name and ISO code.
State: Represents a state/province, linked to a Country via a foreign key.
District: Represents a district, linked to a State via a foreign key.

Notes

The library automatically populates sample data for countries, states, and districts during migrations.
Ensure your Django project uses a compatible version (Django 3.2 or higher).
