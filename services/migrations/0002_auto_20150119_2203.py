# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='maximum_cost',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='minimum_cost',
            field=models.IntegerField(blank=True),
        ),
    ]
