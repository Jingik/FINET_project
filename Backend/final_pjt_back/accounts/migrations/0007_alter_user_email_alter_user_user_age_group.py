# Generated by Django 4.2.7 on 2024-05-18 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_remove_user_groups_remove_user_is_active_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_age_group',
            field=models.CharField(choices=[('10s', '10대'), ('20s', '20대'), ('30s', '30대'), ('40s', '40대'), ('50s', '50대')], max_length=3),
        ),
    ]