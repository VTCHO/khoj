# Generated by Django 4.2.5 on 2023-10-18 16:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("database", "0007_remove_conversationprocessorconfig_conversation_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="conversation",
            name="conversation_log",
            field=models.JSONField(default=dict),
        ),
    ]
