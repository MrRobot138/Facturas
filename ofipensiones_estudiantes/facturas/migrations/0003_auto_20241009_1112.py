# Generated by Django 3.2.6 on 2024-10-09 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudiantes', '0002_resumendecuenta_estudiante'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='factura',
            name='id',
        ),
        migrations.AlterField(
            model_name='factura',
            name='idFactura',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]