# Generated by Django 3.2 on 2022-06-21 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(blank=True, max_length=200, null=True)),
                ('last', models.CharField(blank=True, max_length=200, null=True)),
                ('age', models.IntegerField()),
                ('Country', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
