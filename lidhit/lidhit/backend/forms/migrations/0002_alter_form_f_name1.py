# Generated by Django 4.1.5 on 2023-01-10 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("forms", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="form",
            name="f_name1",
            field=models.CharField(
                default="email", max_length=255, verbose_name="Поле email"
            ),
        ),
    ]