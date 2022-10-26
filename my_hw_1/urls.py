from django.contrib import admin
from django.urls import path, re_path
from myapp.views import main, another, main_article, main_new, article
from myapp.views import artice_archive,article_slug, user_number, regex


urlpatterns = [
    path('', main),
    path('article/', another),
    path('article/arhive/', main_article),
    path('users', main_new),
    path('article/<int:article_number>', article),
    path('article/<int:article_number>/archive', artice_archive),
    path('article/<int:article_number>/<slug:slug_text>', article_slug),
    path('users/<int:user_number>', user_number),
    re_path(r'^(?P<text>[0-9a-fA-F]{4}-[0-9a-fA-F]{6}$)', regex),
]
