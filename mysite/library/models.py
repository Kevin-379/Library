from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Book(models.Model):
	title = models.CharField(max_length=50)
	author = models.CharField(max_length=50)
	publisher = models.CharField(max_length=50)
	genre = models.CharField(max_length=50)
	summary = models.TextField()
	ISBN = models.BigIntegerField()
	location = models.CharField(max_length=50)
	availability = models.BooleanField()
	borrowed_until = models.DateField(blank=True, null=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('book_detail', kwargs={'pk': self.pk})
