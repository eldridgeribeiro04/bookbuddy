# Generated by Django 4.1.7 on 2024-05-05 22:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0002_alter_book_author_delete_author"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="completed",
            field=models.BooleanField(default=False),
        ),
    ]
