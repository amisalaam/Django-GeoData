import json
import os
from django.db import migrations

def load_data(apps, schema_editor):
    Country = apps.get_model('django_geo_regions', 'Country')
    State = apps.get_model('django_geo_regions', 'State')
    District = apps.get_model('django_geo_regions', 'District')
    db_alias = schema_editor.connection.alias

    # Load countries
    countries_file = os.path.join(os.path.dirname(__file__), '..', 'data', 'countries.json')
    with open(countries_file, 'r') as f:
        countries_data = json.load(f)
    for country_data in countries_data:
        Country.objects.using(db_alias).create(**country_data)

    # Load states
    states_file = os.path.join(os.path.dirname(__file__), '..', 'data', 'states.json')
    with open(states_file, 'r') as f:
        states_data = json.load(f)
    for state_data in states_data:
        country = Country.objects.using(db_alias).get(code=state_data['country_code'])
        State.objects.using(db_alias).create(name=state_data['name'], country=country)

    # Load districts
    districts_file = os.path.join(os.path.dirname(__file__), '..', 'data', 'districts.json')
    with open(districts_file, 'r') as f:
        districts_data = json.load(f)
    for district_data in districts_data:
        state = State.objects.using(db_alias).get(name=district_data['state_name'], country__code=district_data['country_code'])
        District.objects.using(db_alias).create(name=district_data['name'], state=state)

class Migration(migrations.Migration):
    dependencies = [
        ('django_geo_regions', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_data),
    ]