from django.shortcuts import render, redirect
from django.http import HttpResponse
from .db import students, favorite_films, active


def index(request):
    return render(request, 'main/index.html', {'db': active})


def remove1(request, number):
    active.remove(active[number])
    return render(request, 'main/index.html', {'db': active})


def remove(request, number):
    for i in active:
        if i['id'] == number:
            active.remove(i)
    return redirect('/')
    # active.remove(active[number])
    # return render(request, 'main/index.html', {'db': active})


def index_1(request):
    hobby = 'boxing'
    return render(request, 'main/index.html',
                  {'name': 'Andrei', 'hobby': hobby, 'students': students})


def films(request):
    return render(request, 'films/index.html',
                  {'films': favorite_films})


def pet(request):
    return HttpResponse('I like dogs')


def fullname(request):
    return HttpResponse('Я Мордач Андрій Олегович')


def place(request):
    return HttpResponse('Я знаходжусь в Україні')


def years_old(request):
    return HttpResponse('Мені 14 повних років')


def education(request):
    return HttpResponse('Я вчусь у школі номер 23')


def hobby(request):
    return HttpResponse('Моє хобі це катання на велосипеді')


def else_about_me(request):
    return HttpResponse('Також я люблю вчитися, програмувати і займатися спортом')
