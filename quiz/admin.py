from django.contrib import admin
from .models import Question, Choice, Subject, Word, Music, QuestionAttempt

# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('question', 'choice_text', 'isCorrectAnswer')
    search_fields = ['question__question_text', 'choice_text']


class WordInline(admin.StackedInline):
    model = Word
    extra = 6


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('subject',)
    search_fields = ['subject']
    inlines = [WordInline]


class WordAdmin(admin.ModelAdmin):
    list_display = ('subject', 'vietnamese', 'english')
    search_fields = ('subject__subject', 'vietnamese', 'english')


class MusicAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


class QuestionAttemptAdmin(admin.ModelAdmin):
    list_display = ('user', 'submit_date', 'question', 'answer', 'correctAnswer', 'isCorrectAnswer')
    list_filter = ('submit_date',)
    search_fields = ('user__username', 'question', 'answer', 'correctAnswer')


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Word, WordAdmin)
admin.site.register(Music, MusicAdmin)
admin.site.register(QuestionAttempt, QuestionAttemptAdmin)