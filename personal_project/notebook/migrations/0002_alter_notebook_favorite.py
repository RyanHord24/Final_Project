# Generated by Django 4.2.16 on 2024-12-10 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('favorites', '0002_favoritecountry_favoritelist_remove_favorite_country_and_more'),
        ('notebook', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notebook',
            name='favorite',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notebooks', to='favorites.favoritecountry'),
        ),
    ]