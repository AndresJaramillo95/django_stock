from django.db import models

# Create your models here. AKA databases. uses classes() to create database.
# two step method:
# create class, then migrate over 

class Stock(models.Model):
	ticker = models.CharField(max_length=10)

	def __str__(self):
		return self.ticker
