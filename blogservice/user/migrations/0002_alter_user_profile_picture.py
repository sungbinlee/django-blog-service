# Generated by Django 4.2.3 on 2023-07-20 12:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="profile_picture",
            field=models.ImageField(blank=True, upload_to="images/"),
        ),
    ]
