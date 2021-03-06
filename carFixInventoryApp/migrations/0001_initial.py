# Generated by Django 4.0.3 on 2022-03-28 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mechanic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mechanic_name', models.CharField(max_length=100)),
                ('garage_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ShopInventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_part', models.CharField(default='mcarFix', max_length=100)),
                ('price_of_part', models.DecimalField(decimal_places=2, max_digits=10)),
                ('car_make', models.CharField(choices=[('toyota', 'toyota'), ('vits', 'vits'), ('tsunami', 'tsunami'), ('isuzu', 'isuzu'), ('Nissan', 'Nissan')], default='toyota', max_length=50)),
                ('car_model', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complexity', models.IntegerField()),
                ('title', models.CharField(max_length=100)),
                ('duration', models.IntegerField()),
                ('mechanic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='carFixInventoryApp.mechanic')),
            ],
            options={
                'ordering': ['complexity'],
                'unique_together': {('mechanic', 'complexity')},
            },
        ),
    ]
