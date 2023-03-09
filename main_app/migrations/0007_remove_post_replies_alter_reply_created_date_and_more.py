# Generated by Django 4.1.7 on 2023-03-09 19:50

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_post_replies_alter_reply_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='replies',
        ),
        migrations.AlterField(
            model_name='reply',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='reply',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='main_app.post'),
        ),
    ]
