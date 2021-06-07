# Generated by Django 3.2.4 on 2021-06-06 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AvocadoData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observation_date', models.DateTimeField()),
                ('sold_plu_4046', models.IntegerField()),
                ('sold_plu_4225', models.IntegerField()),
                ('sold_plu_4770', models.IntegerField()),
                ('small_bags', models.IntegerField()),
                ('large_bags', models.IntegerField()),
                ('xlarge_bags', models.IntegerField()),
                ('organic', models.BooleanField()),
                ('region', models.CharField(max_length=50)),
                ('actual_average_price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='AvocadoPricePrediction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('predicted_average_price', models.FloatField()),
                ('prediction_date', models.DateTimeField()),
                ('avocado_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prediction.avocadodata')),
            ],
        ),
    ]
