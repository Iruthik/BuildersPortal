# Generated by Django 3.2.9 on 2022-02-07 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('use', '0005_supplier'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
            ],
        ),
    ]
