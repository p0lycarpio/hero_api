# Generated by Django 3.2.7 on 2021-09-23 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heroapi', '0002_auto_20210915_0902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publisher',
            name='creator',
            field=models.CharField(max_length=80, unique=True),
        ),
    ]
