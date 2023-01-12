from django.shortcuts import render

def index(request):
    context = {
        'title': 'KinderLife',
    }
    return render(request, 'kinderlife/index.html', context)


def crm(request):
    context = {
        'title': 'CRM',
    }
    return render(request, 'kinderlife/crm/crm.html', context)


def storage(request):
    context = {
        'title': 'Склад',
    }
    return render(request, 'kinderlife/storage/storage.html', context)


def login(request):
    context = {
        'title': 'Авторизация',
    }
    return render(request, 'kinderlife/login.html', context)
