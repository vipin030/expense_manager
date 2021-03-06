# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-01-18 18:48
from __future__ import unicode_literals

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
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(default=0.0)),
                ('payee', models.CharField(max_length=100)),
                ('payment_type', models.CharField(choices=[('C', 'Cash'), ('M', 'Master Card'), ('D', 'Visa'), ('CH', 'Cheque')], max_length=1)),
                ('payment_date', models.DateField()),
                ('description', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('C', 'Done'), ('P', 'Pending')], max_length=1)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='expenseapp.Category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
