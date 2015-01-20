# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_auto_20150119_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='maximum_cost',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='minimum_cost',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
