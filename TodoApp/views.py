import time
from datetime import datetime
from django.db.models import Q
from django.shortcuts import render
from TodoApp.models import TaskList
from django.urls import reverse
from django.http import HttpResponseRedirect


# Create your views here.


def add_task(request):
    t_name = request.POST['tname']
    t_date = request.POST['dtime']
    t_status = request.POST['tstatus']
    query = TaskList(task_name=t_name, end_date=t_date, status=t_status)
    query.save()
    return HttpResponseRedirect(reverse('added'))


def add(request):
    return render(request, 'TodoApp/addtask.html')


def done(request):
    return render(request, 'TodoApp/success.html')


def get_tasks(request):
    query = TaskList.objects.all()
    context = {'query': query}
    return render(request, 'TodoApp/display.html', context)


def update(request, idn):
    query = TaskList.objects.get(id=idn)
    context = {'query': query}
    return render(request, 'TodoApp/update.html', context)


def recordupdate(request, idn):
    query = TaskList.objects.get(id=idn)
    query.task_name = request.POST["task_name"]
    month_date = request.POST["end_date"]
    date_month = month_date.split(" ")
    month=date_month[0]
    day = date_month[1]
    year= date_month[2]
    query.end_date = datetime.strptime(day[:-1]+" "+month+" "+year[:-1], "%d %B %Y")
    query.status = request.POST["status"]
    query.save()
    return HttpResponseRedirect(reverse('display'))


def delete_task(request,idn):
    query = TaskList.objects.get(id=idn)
    query.delete()
    return HttpResponseRedirect(reverse('display'))


def index_view(request):
    return render(request, "TodoApp/index.html")


def pending_tasks(request):
    query = TaskList.objects.filter(Q(status='no') | Q(status='NO'))
    context = {'query': query}
    return render(request, 'TodoApp/display.html', context)


def completed_tasks(request):
    query = TaskList.objects.filter(status='yes')
    context = {'query': query}
    return render(request, 'TodoApp/display.html', context)