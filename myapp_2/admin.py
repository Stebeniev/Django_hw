from django.contrib import admin
from .models import Author, Book,Book_card, User_name

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Book_card)
admin.site.register(User_name)
