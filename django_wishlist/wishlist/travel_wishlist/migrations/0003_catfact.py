# Generated by Django 3.1.2 on 2020-11-18 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel_wishlist', '0002_auto_20201110_2102'),
    ]

    operations = [
        migrations.CreateModel(
            name='CatFact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fact', models.CharField(max_length=500)),
            ],
        ),
    ]