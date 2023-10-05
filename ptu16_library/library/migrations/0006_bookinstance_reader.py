# Generated by Django 4.2.5 on 2023-10-05 10:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('library', '0005_book_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinstance',
            name='reader',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='reader'),
        ),
    ]
