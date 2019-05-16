import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import Choice, Question, Subject, Word, Music, QuestionAttempt

# Create your views here.

def IndexView(request):    
    return render(request, 'quiz/index.html', {})


def RegisterView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # messages.success(request, 'Account created successfully')
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'quiz/register.html', {'form': form})


def LoginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'quiz/login.html', {'form': form})


def LogoutRequest(request):
    logout(request)
    return redirect('index')


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
        user = request.user
        ques = question
        answer = selected_choice
        correctAnswer = question.choice_set.get(isCorrectAnswer=True)
        isCorrectAnswer = (answer == correctAnswer)
        temp = QuestionAttempt(user=user, question=question.question_text, answer=answer.choice_text, 
                               correctAnswer=correctAnswer.choice_text, isCorrectAnswer=isCorrectAnswer)
        temp.save()

        # return HttpResponseRedirect(reverse('question_result', args=(question.id, )))
        return render(request, 'quiz/question_result.html', 
                     {'question_id': question_id, 'isCorrectAnswer': isCorrectAnswer, 'question': question,
                      'correctAnswer': correctAnswer})


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


def HistoryListView(request):
    if not request.user.is_authenticated:
        return render(request, 'quiz/index.html', {'error_message': "Sorry, you must logged in before you can use this feature."})

    username = request.user.username
    history_list = QuestionAttempt.objects.filter(user=request.user).order_by('-submit_date')

    return render(request, 'quiz/history_list.html', {'username': username, 'history_list': history_list})