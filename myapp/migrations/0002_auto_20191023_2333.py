# Generated by Django 2.2.1 on 2019-10-23 18:03

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='user',
            field=models.OneToOneField(on_delete='CASCADE', related_name='type', to=settings.AUTH_USER_MODEL),
        ),
    ]