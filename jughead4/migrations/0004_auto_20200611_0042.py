# Generated by Django 2.2.12 on 2020-06-11 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jughead4', '0003_post_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='R10',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='R11',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='R4',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='R5',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='R6',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='R7',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='R8',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='R9',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='R1',
            field=models.IntegerField(default=0),
        ),
    ]
