# Generated by Django 4.1.7 on 2023-03-30 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_car_license_plate'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecialMarks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Отметка')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars_special_marks', to='cars.car')),
            ],
            options={
                'verbose_name': 'Особая метка',
                'verbose_name_plural': 'Особые метки',
            },
        ),
        migrations.CreateModel(
            name='PeriodsOwnership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_date', models.DateField(verbose_name='От')),
                ('before_date', models.DateField(verbose_name='До')),
                ('actual', models.DateField(default=False, verbose_name='Актуальность')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars_special_ownership', to='cars.car')),
            ],
            options={
                'verbose_name': 'Период владения',
                'verbose_name_plural': 'Периоды владения',
            },
        ),
    ]