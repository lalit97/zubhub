# Generated by Django 3.2.7 on 2021-10-02 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creators', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creator',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
    ]
