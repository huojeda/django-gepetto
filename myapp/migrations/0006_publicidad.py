# Generated by Django 5.2 on 2025-05-01 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_categoria_rename_nombre_cliente_nombre_cliente_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publicidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('imagen_nombre', models.CharField(max_length=100)),
            ],
        ),
    ]
