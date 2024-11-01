# Generated by Django 3.2 on 2021-09-23 09:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TransactionDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(default='', max_length=200)),
                ('renter', models.CharField(default='', max_length=200)),
                ('subPeriod', models.IntegerField(default=3)),
                ('monthlyCharge', models.IntegerField(default=100)),
                ('deposite', models.IntegerField()),
                ('address', models.CharField(max_length=300)),
                ('rentee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
