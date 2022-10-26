from django.http import HttpResponse


def main(request):
    return HttpResponse("Hi! It's your main view!!")

def another(request):
    return HttpResponse("Hi, It's another page!!")

def main_article(request):
    return HttpResponse('Hi, There will be a list with articles')

def main_new(request):
    return HttpResponse("Hi! Users!!")

def article(request, article_number):
    return HttpResponse(f"Hi, {article_number} article")

def artice_archive(request, article_number):
    return HttpResponse (f"Hi, {article_number} article, archive")

def article_slug(request, article_number, slug_text):
    return HttpResponse (f"Hi, {article_number}  {slug_text} ")

def user_number(request, user_number):
    return HttpResponse (f"Hi, {user_number}")

def regex(request, text):
    return HttpResponse(f"Hi, it's regex with text: {text}")