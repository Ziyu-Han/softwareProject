# Generated by Django 4.1 on 2024-06-07 13:39

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="UserInfo",
            fields=[
                (
                    "userId",
                    models.CharField(max_length=20, primary_key=True, serialize=False),
                ),
                ("userName", models.CharField(max_length=20)),
                ("userPwd", models.CharField(max_length=20)),
            ],
        ),
    ]
