import datetime
import os

from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


def upload_location_for_word(instance, filename):
    return "%s/%s/%s" %('word', instance.english, filename)


def upload_location_for_subject(instance, filename):
    return "%s/%s/%s" %('subject', instance.subject, filename)


def upload_location_for_music(instance, filename):
    return "%s/%s/%s" %('music', instance.title, filename)


def validate_image_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.svg']
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Unsupported file extension, please use .jpg, .jpeg, .png, .gif or .svg instead')


def validate_audio_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.mp3', '.ogg', '.wav']
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Unsupported file extension, please use .mp3, .ogg or .wav instead')


def validate_video_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.mp4', '.ogg', '.webm']
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Unsupported file extension, please use .mp4, .ogg or .webm instead')


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', default=datetime.datetime.now)

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    isCorrectAnswer = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text

    def is_correct_answer(self):
        return self.isCorrectAnswer

    is_correct_answer.admin_order_field = 'isCorrectAnswer'
    is_correct_answer.boolean = True
    is_correct_answer.short_description = 'Correct answer?'


class Subject(models.Model):
    subject = models.CharField(max_length=200, unique=True)
    image = models.FileField(upload_to=upload_location_for_subject, default='', validators=[validate_image_extension])
    
    def __str__(self):
        return self.subject


class Word(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    vietnamese = models.CharField(max_length=200)
    english = models.CharField(max_length=200)
    image = models.FileField(upload_to=upload_location_for_word, validators=[validate_image_extension])
    audio = models.FileField(upload_to=upload_location_for_word, validators=[validate_audio_extension])

    def __str__(self):
        return self.english


class Music(models.Model):
    title = models.CharField(max_length=200)
    video = models.FileField(upload_to=upload_location_for_music, validators=[validate_video_extension])

    def __str__(self):
        return self.title