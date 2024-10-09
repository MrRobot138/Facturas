# Generated by Django 3.2.6 on 2024-10-09 01:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Institucion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ResumenDeCuenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=50)),
                ('saldo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('saldoPendiente', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fechaUltimaPago', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='ReciboDePago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idRecibo', models.CharField(max_length=50)),
                ('fechaPago', models.DateField()),
                ('valorCancelado', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tipoDePago', models.CharField(max_length=50)),
                ('ccDelResponsable', models.IntegerField()),
                ('entidadBancaria', models.CharField(max_length=100)),
                ('resumenDeCuenta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estudiantes.resumendecuenta')),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('codigo', models.CharField(max_length=50)),
                ('grado', models.CharField(max_length=50)),
                ('institucion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estudiantes.institucion')),
            ],
        ),
    ]
