# Generated by Django 2.1.3 on 2018-11-28 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('positivepets', '0007_auto_20181128_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='picture',
            field=models.FileField(blank=True, null=True, upload_to='media/'),
        ),
    ]