# Generated by Django 4.2.3 on 2023-08-03 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('it_pojmy', '0003_komentar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clanek',
            name='datum',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
