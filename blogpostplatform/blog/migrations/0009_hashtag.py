# Generated by Django 5.0.7 on 2024-08-05 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_vote_is_liked'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('posts', models.ManyToManyField(to='blog.post')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
