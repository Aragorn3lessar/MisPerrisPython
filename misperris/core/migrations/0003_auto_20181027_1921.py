# Generated by Django 2.1.2 on 2018-10-27 22:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20181026_1212'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('name', models.CharField(max_length=45, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('name', models.CharField(max_length=45, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Socio',
            fields=[
                ('name', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('correo', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=245)),
                ('fecha_n', models.DateField()),
                ('telefono', models.IntegerField()),
                ('contrasena', models.CharField(max_length=100)),
                ('ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Ciudad')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Region')),
            ],
        ),
        migrations.CreateModel(
            name='TipoUser',
            fields=[
                ('name', models.CharField(max_length=45, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Vivienda',
            fields=[
                ('name', models.CharField(max_length=45, primary_key=True, serialize=False)),
            ],
        ),
        migrations.AlterField(
            model_name='mascota',
            name='foto',
            field=models.ImageField(upload_to='', verbose_name=models.ImageField(upload_to='static/core/img')),
        ),
        migrations.AddField(
            model_name='socio',
            name='tipo_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.TipoUser'),
        ),
        migrations.AddField(
            model_name='socio',
            name='tipo_viv',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Vivienda'),
        ),
        migrations.AddField(
            model_name='ciudad',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Region'),
        ),
    ]
