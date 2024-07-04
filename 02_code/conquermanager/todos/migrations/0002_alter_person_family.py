# Generated by Django 5.0.6 on 2024-06-28 05:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todos", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="person",
            name="family",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="persons",
                to="todos.family",
            ),
        ),
    ]