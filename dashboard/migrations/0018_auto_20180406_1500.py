# Generated by Django 2.0.2 on 2018-04-06 13:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('dashboard', '0017_auto_20180406_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentreviewitem',
            name='rate',
            field=models.PositiveSmallIntegerField(),
        ),
    ]