# Generated by Django 3.1.2 on 2020-12-30 07:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paradign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Programmer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('languages', models.ManyToManyField(to='lan.Language')),
            ],
        ),
        migrations.AlterField(
            model_name='language',
            name='paradign',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lan.paradign'),
        ),
    ]
