# Generated by Django 2.0.6 on 2018-06-19 01:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login_registration', '0002_remove_user_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='TVShow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_url', models.CharField(max_length=128, unique=True)),
                ('api_id', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=64)),
                ('image', models.CharField(max_length=64)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='TVShowLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('tvshow', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes_by', to='tvshow.TVShow')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='login_registration.User')),
            ],
        ),
    ]
