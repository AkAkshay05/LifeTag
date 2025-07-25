# Generated by Django 5.1.6 on 2025-07-06 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xcape', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='xcape',
            name='address',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='xcape',
            name='allergies',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='xcape',
            name='blood_type',
            field=models.CharField(default=1, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='xcape',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='xcape',
            name='guardian_phone',
            field=models.CharField(default=1.0, max_length=15),
            preserve_default=False,
        ),
    ]
