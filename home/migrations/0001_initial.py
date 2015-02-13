# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomePageText',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('page_text', models.CharField(max_length=2500, null=True)),
                ('is_active', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
