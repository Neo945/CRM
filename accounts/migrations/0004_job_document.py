# Generated by Django 4.0.5 on 2022-06-26 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_profile_email_profile_first_name_profile_last_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='document',
            field=models.FileField(default='https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf', max_length=30, upload_to=''),
            preserve_default=False,
        ),
    ]