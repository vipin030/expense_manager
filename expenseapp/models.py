from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name


class Expense(models.Model):
	PAYMENT_CHOICES = (
		('C', 'Cash'),
		('M', 'Master Card'),
		('D', 'Visa'),
		('CH', 'Cheque')
	)
	STATUS_CHOICES = (
		('C', 'Done'),
		('P', 'Pending')
	)
	amount = models.FloatField(default=0.0)
	payee = models.CharField(max_length=100)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
	payment_type = models.CharField(max_length=1, choices=PAYMENT_CHOICES)
	payment_date = models.DateField()
	description = models.CharField(max_length=255)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	status = models.CharField(max_length=1, choices=STATUS_CHOICES)