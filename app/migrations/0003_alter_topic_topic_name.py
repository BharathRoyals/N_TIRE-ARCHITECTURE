# Generated by Django 4.1.7 on 2023-04-02 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_topic_topic_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='topic_name',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
