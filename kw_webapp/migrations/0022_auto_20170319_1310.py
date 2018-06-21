# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-19 17:10
from __future__ import unicode_literals

from django.db import migrations, models
import kw_webapp.constants


class Migration(migrations.Migration):

    dependencies = [("kw_webapp", "0021_userspecific_critical")]

    operations = [
        migrations.RemoveField(model_name="profile", name="only_review_burned"),
        migrations.AddField(
            model_name="profile",
            name="minimum_wk_srs_level_to_review",
            field=models.CharField(
                choices=[
                    ("APPRENTICE", "apprentice"),
                    ("GURU", "guru"),
                    ("MASTER", "master"),
                    ("ENLIGHTENED", "enlightened"),
                    ("BURNED", "burned"),
                ],
                default="APPRENTICE",
                max_length=20,
            ),
        ),
    ]
