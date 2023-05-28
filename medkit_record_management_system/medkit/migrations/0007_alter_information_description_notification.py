# Generated by Django 4.2 on 2023-04-09 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("medkit", "0006_remove_post_author_information_description_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="information",
            name="description",
            field=models.CharField(default="", max_length=30),
        ),
        migrations.CreateModel(
            name="Notification",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("message", models.CharField(max_length=225)),
                ("created_at", models.DateTimeField(auto_now=True)),
                (
                    "medkit",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="medkit.information",
                    ),
                ),
            ],
        ),
    ]