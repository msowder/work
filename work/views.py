from django.shortcuts import get_object_or_404, render

from .models import Tasks, Rewards, Calendar, Account

from django.http import HttpResponse

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    latest_question_list = Tasks.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def vote(request, question_id):
    latest_question_list = Tasks.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

# def get_tasks():
#     a_list = Tasks.objects.filter(pub_date__year=year)
#     context = {'year': year, 'article_list': a_list}
#     return render(request, 'news/year_archive.html', context)
