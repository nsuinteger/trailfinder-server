# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rentlet_user', '0001_initial'),
        ('item', '0002_auto_20141206_1011'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='created_by',
            field=models.ForeignKey(related_name='creator', default=1, to='rentlet_user.RentletUser'),
            preserve_default=False,
        ),
    ]
