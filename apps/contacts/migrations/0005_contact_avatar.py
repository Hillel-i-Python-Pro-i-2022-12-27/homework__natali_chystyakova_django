# Generated by Django 4.1.5 on 2023-02-17 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contacts", "0004_alter_contact_operator"),
    ]

    operations = [
        migrations.AddField(
            model_name="contact",
            name="avatar",
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to="contacts/contact/avatar/"),
        ),
    ]
