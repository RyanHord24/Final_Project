# Generated by Django 4.2.16 on 2024-12-11 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('favorites', '0005_remove_favoritecountry_favorite_country_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favoritecountry',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
