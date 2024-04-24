# Generated by Django 5.0.4 on 2024-04-24 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(max_length=100)),
                ('order_number', models.CharField(max_length=150)),
                ('date', models.DateField()),
                ('status', models.CharField(max_length=100)),
            ],
        ),
    ]
