# Generated by Django 4.2.4 on 2023-08-26 17:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("airport", "0005_flight_crew"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ticket",
            name="row",
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name="ticket",
            name="seat",
            field=models.PositiveIntegerField(),
        ),
    ]
