# Generated by Django 4.2.13 on 2024-05-30 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management_app', '0006_alter_payment_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='management_app.people'),
        ),
    ]
