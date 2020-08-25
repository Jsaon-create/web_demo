# Generated by Django 3.0.8 on 2020-08-17 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nanjing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('each_price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'db_table': 'nanjing',
                'managed': False,
            },
        ),
    ]