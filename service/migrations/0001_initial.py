# Generated by Django 4.2.7 on 2023-11-10 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=15)),
                ('gender', models.CharField(max_length=10)),
                ('pickup_location', models.CharField(max_length=250)),
                ('drop_location', models.CharField(max_length=250)),
                ('pickup_time', models.TimeField()),
                ('return_time', models.TimeField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='SelectedDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='OfficeBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=15)),
                ('gender', models.CharField(max_length=10)),
                ('pickup_location', models.CharField(max_length=250)),
                ('drop_location', models.CharField(max_length=250)),
                ('pickup_time', models.TimeField()),
                ('return_time', models.TimeField()),
                ('want_return', models.BooleanField(default=False)),
                ('selected_days', models.ManyToManyField(blank=True, to='service.selectedday')),
            ],
        ),
    ]
