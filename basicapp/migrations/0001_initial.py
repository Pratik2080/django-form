# Generated by Django 3.1.4 on 2021-01-11 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=20)),
                ('verify_email', models.EmailField(max_length=20)),
                ('mobile_no', models.IntegerField()),
                ('pan_no', models.CharField(max_length=10)),
                ('dob', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lenden',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('principal', models.IntegerField()),
                ('rate', models.FloatField()),
                ('time', models.IntegerField()),
                ('total_amount', models.FloatField()),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basicapp.userinfo')),
            ],
        ),
    ]