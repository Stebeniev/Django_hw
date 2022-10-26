from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=200, default='')
    last_name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.first_name

class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.name










