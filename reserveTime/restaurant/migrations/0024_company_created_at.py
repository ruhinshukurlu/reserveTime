# Generated by Django 3.0.8 on 2020-08-31 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0023_auto_20200830_0741'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='created_at',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Created date'),
        ),
    ]
