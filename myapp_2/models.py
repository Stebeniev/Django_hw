from django.db import models

class Author(models.Model):
    first_name = models.CharField (max_length=200, default='')
    last_name = models.CharField (max_length=200, null=True, blank=True)

    def __str__(self):
        return self.first_name

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return self.title

class Book_card(models.Model):
    name_of_book = models.CharField(max_length=200, default='')
    user = models.CharField(max_length=200, null=True, blank=True)
    issued = models.DateField(null=True, blank=True)
    surrendered = models.DateField(null=True, blank=True)
    book_cards = models.ManyToManyField(Book)

class User_name(models.Model):
    name = models.ForeignKey(Book_card, on_delete=models.CASCADE, null=True, related_name='User_names')




    def __str__(self):
        return self.name_of_book





