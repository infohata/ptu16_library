# Generated by Django 4.2.5 on 2023-10-03 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_alter_bookinstance_unique_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='bio',
            field=models.TextField(blank=True, default='', max_length=4000, verbose_name='Bio'),
        ),
    ]
