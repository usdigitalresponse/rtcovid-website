# Generated by Django 3.0.5 on 2020-04-02 13:01

from django.db import migrations
from django.conf import settings

import csv, os

def load_states(apps, schema_editor):
    State = apps.get_model('dashboard', 'State',)
    with open(
        os.path.join(settings.BASE_DIR, 'apps', 'dashboard', 'data', 'states.csv'),
        encoding='utf-8-sig',
    ) as state_csv:
        reader = csv.DictReader(state_csv)
        for row in reader:
            State.objects.create(name=row['Name'], code=row['Code'], population=row['Population'])

def remove_states(apps, schema_editor):
    State = apps.get_model('dashboard', 'State',)
    State.objects.all().delete()

def load_counties(apps, schema_editor):
    State = apps.get_model('dashboard', 'State')
    County = apps.get_model('dashboard', 'County')

    with open(
        os.path.join(settings.BASE_DIR, 'apps', 'dashboard', 'data', 'counties.csv'),
        encoding='utf-8-sig',
    ) as county_csv:
        reader = csv.DictReader(county_csv)
        for row in reader:
            state = State.objects.get(name=row['State'])
            County.objects.create(name=row['Name'], state=state, population=row['Population'])

def remove_counties(apps, schema_editor):
    County = apps.get_model('dashboard', 'County',)
    County.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_states, remove_states),
        migrations.RunPython(load_counties, remove_counties),
    ]
