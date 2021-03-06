# Generated by Django 3.0.3 on 2020-03-04 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('type', models.IntegerField(choices=[(1, 'Верх'), (2, 'Низ'), (3, 'Не выбран')])),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='ProductSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('bottom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bottom', to='main.Product')),
                ('top', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='top', to='main.Product')),
            ],
        ),
    ]
