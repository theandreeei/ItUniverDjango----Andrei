from django.shortcuts import render, redirect
from django.http import HttpResponse
from .db import students, favorite_films, active, completed_list
from random import randint
from datetime import date


def index(request):
    save_to_file()
    return render(request, 'main/index.html', {'db': active, 'title': 'Active'})


def add(request):
    if request.method == 'GET':
        return render(request, 'main/add.html')
    description = request.POST.get('description')
    title = request.POST.get('title')
    active.append({
        'id': randint(0, 10000),
        'Title': title,
        'Description': description,
        'Date': date.today().strftime('%d.%m.%Y')
    })
    return redirect('/')


def remove1(request, number):
    active.remove(active[number])
    return render(request, 'main/index.html', {'db': active})


def remove(request, number):
    for i in active:
        if i['id'] == number:
            completed_list.append(i)
            active.remove(i)
            break
    return redirect('/')


def save_to_file():
    with open('data.txt', 'w', encoding='utf-8') as file:
        for task in active:
            file.write(f"{task['id']}\t{task['Title']}\t{task['Description']}\t{task['Date']}\n")


def completed(request):
    return render(request, 'main/index.html', {'db': completed_list, 'title': 'Completed'})


def info(request, number):
    for i in active + completed_list:
        if i['id'] == number:
            return render(request, 'main/single.html', {'task': i})


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
