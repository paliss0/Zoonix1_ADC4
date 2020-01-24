from django.db import models
from datetime import datetime


# Create your models here.
class Parlour(models.Model):
	parlour_name = models.CharField(max_length =100)
	parlour_description = models.TextField()
	date = models.DateTimeField('date')
	pdf = models.FileField(upload_to="book/pdfs")




