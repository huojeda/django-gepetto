# Generated by Django 5.2 on 2025-04-21 03:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_remove_comuna_region_alter_comuna_nombre_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id_categoria', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_categoria', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.RenameField(
            model_name='cliente',
            old_name='nombre',
            new_name='nombre_cliente',
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_producto', models.CharField(max_length=200)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock', models.PositiveIntegerField()),
                ('nombre_categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.categoria')),
            ],
        ),
    ]
