# Generated by Django 4.0.1 on 2022-05-07 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='status',
            field=models.CharField(choices=[('OP', 'opened'), ('FI', 'finished')], default='OP', max_length=2),
        ),
    ]
