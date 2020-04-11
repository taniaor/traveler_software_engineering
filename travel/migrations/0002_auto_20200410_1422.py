# Generated by Django 3.0.3 on 2020-04-10 21:22

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(max_length=30)),
                ('title', models.TextField(max_length=30)),
                ('description', models.TextField(max_length=30)),
                ('created', models.DateField(auto_now=True)),
                ('updated', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=30)),
                ('stars', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('feedback', models.TextField(blank=True, max_length=200)),
                ('created', models.DateField(auto_now=True)),
                ('updated', models.DateField(auto_now=True)),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel.Destination')),
                ('traveler', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel.Traveler')),
            ],
            options={
                'unique_together': {('traveler', 'destination')},
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.TextField(max_length=30)),
                ('city', models.TextField(max_length=30)),
                ('zip_code', models.TextField(max_length=10)),
                ('created', models.DateField(auto_now=True)),
                ('updated', models.DateField(auto_now=True)),
                ('is_my_location', models.BooleanField(default=False)),
                ('is_visiting', models.BooleanField(default=False)),
                ('traveler', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel.Traveler')),
            ],
        ),
        migrations.AddField(
            model_name='destination',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel.Location'),
        ),
        migrations.AddField(
            model_name='destination',
            name='traveler',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel.Traveler'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(max_length=100)),
                ('input', models.TextField(blank=True, max_length=100)),
                ('output', models.TextField(blank=True, max_length=100)),
                ('created', models.DateField(auto_now=True)),
                ('updated', models.DateField(auto_now=True)),
                ('review', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='travel.Review')),
                ('traveler', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='travel.Traveler')),
            ],
        ),
    ]