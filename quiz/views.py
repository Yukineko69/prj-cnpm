from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .models import Choice, Question, Subject, Word, Music

# Create your views here.

def IndexView(request):
    return render(request, 'quiz/index.html', {})


class QuestionListView(generic.ListView):
    template_name = 'quiz/question_list.html'
    context_object_name = 'question_list'

    def get_queryset(self):
        return Question.objects.order_by('?')[:1]


class QuestionDetailView(generic.DetailView):
    model = Question
    template_name = 'quiz/question_detail.html'
    context_object_name = 'question'

    def get_queryset(self):
        return Question.objects.all()


class QuestionResultView(generic.DetailView):
    model = Question
    template_name = 'quiz/question_result.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'quiz/question_detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('question_result', args=(question.id, )))


class SubjectListView(generic.ListView):
    template_name = 'quiz/subject_list.html'
    context_object_name = 'subject_list'

    def get_queryset(self):
        return Subject.objects.all()


class SubjectDetailView(generic.DetailView):
    model = Subject
    template_name = 'quiz/subject_detail.html'
    context_object_name = 'subject'

    def get_querySet(self):
        return Subject.objects.all()


class MusicListView(generic.ListView):
    template_name = 'quiz/music_list.html'
    context_object_name = 'music_list'

    def get_queryset(self):
        return Music.objects.all()


class MusicDetailView(generic.DetailView):
    template_name = 'quiz/music_detail.html'
    context_object_name = 'music'

    def get_queryset(self):
        return Music.objects.all()