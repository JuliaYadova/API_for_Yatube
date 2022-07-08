# Generated by Django 2.2.16 on 2022-03-17 18:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0002_auto_20220317_2059"),
    ]

    operations = [
        migrations.CreateModel(
            name="Group",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("slug", models.SlugField(unique=True)),
                ("description", models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name="post",
            name="group",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="posts.Group",
            ),
        ),
    ]