# Generated by Django 2.1.5 on 2019-01-06 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PowerPlant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plant_name', models.CharField(help_text='The name power plant concerned .e.g. Limbe Power Plant(LPP).', max_length=1000, verbose_name='Power Plant Name')),
                ('location', models.CharField(help_text='The location of the Power Plant.', max_length=1000, verbose_name='Location')),
                ('production_capacity', models.FloatField(default=0, help_text='The production capacity of the Power Plant in MW(Mega Watt).', max_length=1000, verbose_name='Production Capacity')),
                ('power_category', models.PositiveIntegerField(choices=[(1, 'Hydro'), (2, 'Thermal'), (3, 'Other')], help_text='The category of the Power Plant .i.e. hydro or thermal', verbose_name='Category')),
                ('placement_priority', models.PositiveIntegerField(default=1, help_text='The order of the Power Plant placement for generation.', verbose_name='Placement Priority')),
                ('grouping', models.CharField(blank=True, editable=False, help_text='The group to which Power Plant belongs.', max_length=1000, null=True, verbose_name='Grouping')),
            ],
            options={
                'verbose_name': 'Power Plant',
                'verbose_name_plural': 'Power Plants',
            },
        ),
    ]