# Generated by Django 3.1.5 on 2021-01-25 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('artists', models.CharField(max_length=100)),
                ('genre', models.TextField(max_length=100)),
                ('year', models.IntegerField()),
            ],
        ),
    ]
