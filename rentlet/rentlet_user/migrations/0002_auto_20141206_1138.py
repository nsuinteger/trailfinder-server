# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rentlet_user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rentletuser',
            name='password',
        ),
        migrations.RemoveField(
            model_name='rentletuser',
            name='username',
        ),
        migrations.AddField(
            model_name='rentletuser',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
