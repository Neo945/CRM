# Generated by Django 4.0.5 on 2022-06-25 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0006_alter_marketinglead_approved_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='leads',
            name='is_done',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='marketinglead',
            name='is_done',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='operationlead',
            name='is_done',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='presaleslead',
            name='is_done',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='saleslead',
            name='is_done',
            field=models.BooleanField(default=False),
        ),
    ]