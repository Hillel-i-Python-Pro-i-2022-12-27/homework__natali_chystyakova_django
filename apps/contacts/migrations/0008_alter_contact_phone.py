# Generated by Django 4.1.5 on 2023-02-22 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contacts", "0007_alter_contact_avatar_alter_contact_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="phone",
            field=models.CharField(max_length=100),
        ),
    ]
