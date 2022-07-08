# Generated by Django 2.2.16 on 2022-03-17 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0004_auto_20220318_0029"),
    ]

    operations = [
        migrations.AddConstraint(
            model_name="follow",
            constraint=models.UniqueConstraint(
                fields=("user", "following"), name="unique_following"
            ),
        ),
    ]
