# Generated by Django 4.1.5 on 2023-02-15 22:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("contacts", "0003_alter_contact_operator"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="operator",
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="contacts",
                to="contacts.operator",
            ),
        ),
    ]
