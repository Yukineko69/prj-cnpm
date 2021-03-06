# Generated by Django 2.0.7 on 2019-05-14 05:18

from django.db import migrations, models
import quiz.models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_auto_20190514_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='video',
            field=models.FileField(upload_to=quiz.models.upload_location_for_music, validators=[quiz.models.validate_video_extension]),
        ),
        migrations.AlterField(
            model_name='subject',
            name='image',
            field=models.FileField(default='', upload_to=quiz.models.upload_location_for_subject, validators=[quiz.models.validate_image_extension]),
        ),
        migrations.AlterField(
            model_name='word',
            name='audio',
            field=models.FileField(upload_to=quiz.models.upload_location_for_word, validators=[quiz.models.validate_audio_extension]),
        ),
        migrations.AlterField(
            model_name='word',
            name='image',
            field=models.FileField(upload_to=quiz.models.upload_location_for_word, validators=[quiz.models.validate_image_extension]),
        ),
    ]
