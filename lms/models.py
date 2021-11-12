from django.db import models

# Create your models here.
class lms_admin(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    mobile = models.BigIntegerField()

    class Meta:
        db_table = "lms_admin"

class books(models.Model):
    book_title = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    author = models.CharField(max_length=100)
    language = models.CharField(max_length=30)
    publisher = models.CharField(max_length=100)
    publication_date = models.CharField(max_length=25)
    ISBN = models.BigIntegerField()
    country_of_origin = models.CharField(max_length=40)
    book_photo = models.CharField(max_length=200)

    class Meta:
        db_table = "books"