# Generated by Django 4.1.7 on 2023-03-12 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("django1", "0007_alter_brand_founding_year_alter_brand_name_customers"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customers",
            name="name",
            field=models.CharField(max_length=200),
        ),
    ]
