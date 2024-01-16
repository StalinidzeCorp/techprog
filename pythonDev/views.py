from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def demand(request):
    return render(request, 'demand.html')


def geography(request):
    return render(request, 'geography.html')


def skills(request):
    return render(request, 'skills.html')


def latest(request):
    return render(request, 'latest.html')
