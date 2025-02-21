# Generated by Django 5.1.6 on 2025-02-20 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('PizzaOwner', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('toppings', models.ManyToManyField(to='PizzaOwner.topping')),
            ],
        ),
    ]
