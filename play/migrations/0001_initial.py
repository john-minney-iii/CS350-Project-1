# Generated by Django 3.2.7 on 2021-09-29 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlackCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CardNo', models.IntegerField()),
                ('CardText', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='WhiteCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CardNo', models.IntegerField()),
                ('CardText', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.DecimalField(decimal_places=2, max_digits=4)),
                ('timesAppeared', models.IntegerField(default=0)),
                ('BlackCard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='play.blackcard')),
                ('WhiteCard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='play.whitecard')),
            ],
        ),
    ]
