from django.shortcuts import get_object_or_404, render

from .models import Tasks, Rewards, Account

from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def get_tasks(request, task_id):
    task = get_object_or_404(Tasks, pk=task_id)
    return render(request, 'tasks.html', {'task': task})


def get_rewards(request, reward_id):
    rewards = get_object_or_404(Rewards, pk=reward_id)
    return render(request, 'rewards.html', {'rewards': rewards})


def get_account(request, account_id):
    account = get_object_or_404(Account, pk=account_id)
    return render(request, 'account.html', {'account': account})
