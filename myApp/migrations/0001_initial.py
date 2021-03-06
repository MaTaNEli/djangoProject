# Generated by Django 4.0.3 on 2022-03-18 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CitizenDetails',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('FirstName', models.CharField(max_length=100)),
                ('LastName', models.CharField(max_length=100)),
                ('BirthDay', models.DateField()),
                ('Address', models.CharField(max_length=100)),
                ('City', models.CharField(max_length=100)),
                ('ZipCode', models.IntegerField()),
                ('LandLine', models.CharField(max_length=100)),
                ('Phone', models.IntegerField()),
                ('isInfected', models.BooleanField()),
                ('Conditions', models.CharField(max_length=100)),
            ],
        ),
    ]
