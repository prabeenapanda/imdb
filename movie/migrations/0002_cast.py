# Generated by Django 4.0.2 on 2022-03-03 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('age', models.PositiveIntegerField(null=True)),
                ('gender', models.CharField(choices=[('Male', 'MALE'), ('Female', 'FEMALE'), ('Transgender', 'TRANSGENDER')], max_length=12)),
                ('movie', models.ManyToManyField(related_name='casts', to='movie.Movie')),
            ],
        ),
    ]
