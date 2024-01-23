# Generated by Django 4.2.7 on 2024-01-12 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fauzan', '0003_rename_kategori_produk_kategori_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatID',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chatid', models.CharField(max_length=200, null=True)),
                ('nama', models.CharField(max_length=200, null=True)),
                ('aktif', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Data Chat ID',
            },
        ),
    ]
