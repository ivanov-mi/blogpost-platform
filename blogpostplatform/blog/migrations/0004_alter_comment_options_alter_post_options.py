# Generated by Django 5.0.7 on 2024-08-02 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['date_created']},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['date_posted']},
        ),
    ]
