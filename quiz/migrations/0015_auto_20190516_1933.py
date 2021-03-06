# Generated by Django 2.0.7 on 2019-05-16 12:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0014_questionattempt_iscorrectanswer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionattempt',
            name='answer',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='questionattempt',
            name='correctAnswer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='quiz.Choice'),
        ),
        migrations.AlterField(
            model_name='questionattempt',
            name='question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='quiz.Question'),
        ),
        migrations.AlterField(
            model_name='questionattempt',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
