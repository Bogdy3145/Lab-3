# Generated by Django 4.1.7 on 2023-03-11 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("django1", "0003_brand"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cars",
            name="name",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="django1.brand"
            ),
        ),
    ]
