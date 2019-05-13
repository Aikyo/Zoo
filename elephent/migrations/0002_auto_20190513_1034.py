# Generated by Django 2.1.7 on 2019-05-13 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elephent', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('describe', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='username',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
