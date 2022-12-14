# Generated by Django 2.2.4 on 2022-12-14 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dojo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('city', models.CharField(max_length=60)),
                ('state', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Ninjas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=60)),
                ('dojo_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ninjas', to='appOne.Dojo')),
            ],
        ),
    ]
