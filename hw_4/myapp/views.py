from django.shortcuts import render
from myapp.models import Comment


def index(request):
    data = {
    'coms': Comment.objects.all()[:5]
    }
    return render(request, 'index.html', data)


def second(request):
    data = {
    'coms': Comment.objects.all()[6:11]
    }
    return render(request, 'second.html', data)


# def third(request):
#     coms = Comment.objects.all()[6:]
#     date = Comment.objects.filter(created_at='2021-10-28')
#     return render(request, 'third.html', {'coms': coms}, {'date': date})


# def fourth(request):
#     data = {
#     'coms': Comment.objects.all()[6:11]
#     }
#     return render(request, 'fourth.html', data)