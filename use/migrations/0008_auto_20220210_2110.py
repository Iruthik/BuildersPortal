# Generated by Django 3.2.9 on 2022-02-10 15:40

from django.db import migrations, models
import use.models


class Migration(migrations.Migration):

    dependencies = [
        ('use', '0007_worker_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supplier',
            name='rate',
        ),
        migrations.AddField(
            model_name='supplier',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=use.models.Supplier.get_filename),
        ),
    ]
