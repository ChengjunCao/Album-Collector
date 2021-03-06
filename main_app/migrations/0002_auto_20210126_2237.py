# Generated by Django 3.1.5 on 2021-01-26 22:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='genre',
            field=models.CharField(max_length=100),
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disc', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], default=(1, 1))),
                ('number', models.IntegerField()),
                ('title', models.CharField(max_length=100)),
                ('length', models.CharField(max_length=100)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.album')),
            ],
        ),
    ]
