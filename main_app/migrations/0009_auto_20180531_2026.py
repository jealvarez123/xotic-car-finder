# Generated by Django 2.0.5 on 2018-05-31 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_auto_20180530_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='image',
            field=models.ImageField(default=1, upload_to='car_image'),
            preserve_default=False,
        ),
    ]