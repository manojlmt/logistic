# Generated by Django 5.0.4 on 2024-06-09 06:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log_app', '0003_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='rate',
            name='to_zone',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rates_to', to='log_app.zone'),
        ),
        migrations.AlterField(
            model_name='rate',
            name='from_zone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rates_from', to='log_app.zone'),
        ),
    ]
