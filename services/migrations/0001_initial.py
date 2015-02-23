# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(unique=True, max_length=100)),
                ('minimum_cost', models.IntegerField(null=True, blank=True)),
                ('maximum_cost', models.IntegerField(null=True, blank=True)),
                ('category', models.IntegerField(choices=[(1, 'Haircuts'), (2, 'Colors'), (3, 'Straightening'), (4, 'Perms'), (5, 'Skincare')])),
                ('order', models.IntegerField(unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
