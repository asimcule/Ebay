# Generated by Django 4.2.2 on 2023-09-10 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_alter_listing_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='description',
            field=models.TextField(blank=True, default=None, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='image',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
