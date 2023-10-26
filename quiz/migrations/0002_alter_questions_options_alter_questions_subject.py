# Generated by Django 4.2.6 on 2023-10-21 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='questions',
            options={'verbose_name_plural': 'Question'},
        ),
        migrations.AlterField(
            model_name='questions',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quiz', to='quiz.subjects'),
        ),
    ]
