# Generated by Django 4.1.4 on 2023-01-19 05:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('sno', models.IntegerField()),
                ('dept_no', models.IntegerField(max_length=2, primary_key=True, serialize=False)),
                ('dept_name', models.CharField(max_length=20)),
                ('loc', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sno', models.IntegerField()),
                ('ename', models.CharField(max_length=20, null=True)),
                ('emp_no', models.IntegerField(max_length=5)),
                ('mgr_no', models.IntegerField(max_length=5)),
                ('sal', models.IntegerField(null=True)),
                ('comm', models.IntegerField()),
                ('dept_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.dept')),
            ],
        ),
    ]