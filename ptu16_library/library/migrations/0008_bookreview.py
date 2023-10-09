# Generated by Django 4.2.5 on 2023-10-06 08:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('library', '0007_alter_author_bio_alter_book_summary'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=4000, verbose_name='Content')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='created at')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='library.book', verbose_name='book')),
                ('reviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_reviews', to=settings.AUTH_USER_MODEL, verbose_name='reviewer')),
            ],
            options={
                'verbose_name': 'book review',
                'verbose_name_plural': 'book reviews',
                'ordering': ['-created_at'],
            },
        ),
    ]