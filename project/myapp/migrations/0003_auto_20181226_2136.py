# Generated by Django 2.0 on 2018-12-26 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20181226_2133'),
    ]

    operations = [
        migrations.RenameField(
            model_name='businesstostudentscore',
            old_name='self',
            new_name='himself',
        ),
        migrations.RenameField(
            model_name='zhuanjiatostudentscore',
            old_name='self',
            new_name='himself',
        ),
    ]