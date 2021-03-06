# Generated by Django 3.0.8 on 2020-08-16 13:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('restaurant', '0015_auto_20200814_0701'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='raiting',
        ),
        migrations.AddField(
            model_name='comment',
            name='liked',
            field=models.IntegerField(blank=True, null=True, verbose_name='Like'),
        ),
        migrations.AddField(
            model_name='comment',
            name='ratingAmbience',
            field=models.IntegerField(blank=True, null=True, verbose_name='ratingAmbience'),
        ),
        migrations.AddField(
            model_name='comment',
            name='ratingFood',
            field=models.IntegerField(blank=True, null=True, verbose_name='ratingFood'),
        ),
        migrations.AddField(
            model_name='comment',
            name='ratingService',
            field=models.IntegerField(blank=True, null=True, verbose_name='ratingService'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='reciever',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reciever_notification', to=settings.AUTH_USER_MODEL, verbose_name='Reciever'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='sender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sender_notification', to=settings.AUTH_USER_MODEL, verbose_name='Sender'),
        ),
    ]
