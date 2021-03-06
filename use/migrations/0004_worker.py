# Generated by Django 3.2.9 on 2022-02-05 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('use', '0003_delete_userregister'),
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=2000)),
                ('rate', models.FloatField()),
                ('location', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
                ('availability', models.CharField(max_length=200)),
            ],
        ),
    ]
