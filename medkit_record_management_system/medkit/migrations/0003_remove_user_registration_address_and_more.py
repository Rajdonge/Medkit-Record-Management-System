# Generated by Django 4.1.3 on 2023-03-16 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("medkit", "0002_alter_user_registration_phone_sale_information"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user_registration",
            name="address",
        ),
        migrations.RemoveField(
            model_name="user_registration",
            name="gender",
        ),
        migrations.RemoveField(
            model_name="user_registration",
            name="phone",
        ),
    ]
