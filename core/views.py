from django.shortcuts import get_object_or_404, render

from .models import Tasks, Rewards, Calendar, Account

from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')

def get_tasks(request, task_id):
    task = get_object_or_404(Tasks, pk=task_id)
    context = {'task': task}
    return render(request, 'tasks.html', context)


def get_rewards(request, reward_id):
    reward = get_object_or_404(Rewards, pk=reward_id)
    context = {'rewards': reward_id}
    return render(request, '../work-static/templates/year_archive.html', context)


def get_calendar(request, question_id):
    question = get_object_or_404(Calendar, pk=question_id)
    return render(request, '../work-static/templates/detail.html', {'question': question})


def get_account(request, question_id):
    latest_question_list = Tasks.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, '../work-static/templates/index.html', context)
