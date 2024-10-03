# Generated by Django 5.1.1 on 2024-10-02 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('cuit', models.PositiveBigIntegerField(max_length=11, primary_key=True, serialize=False)),
                ('empresa', models.CharField(max_length=20)),
                ('empleado', models.CharField(max_length=20)),
                ('cargo', models.CharField(max_length=30)),
            ],
        ),
    ]