from django.shortcuts import render

def index(request):
    context = {
        'title': 'KinderLife'
    }
    return render(request, 'kinderlife/index.html', context)
