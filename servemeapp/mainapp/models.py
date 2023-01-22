from django.db import models
from django.core.validators import MinLengthValidator

class Diner(models.Model):
	username = models.CharField(max_length=100, null=True, unique=True)
	password = models.CharField(max_length=100, null=True)
	phone = models.CharField(max_length=10, null=True, validators=[MinLengthValidator(10, "Must have strictly 10 digits")])
	#user = models.OneToOneField(User, on_delete=models.CASCADE)
	def __str__(self):
		return self.username

class Manager(models.Model):
	username = models.CharField(max_length=100, null=True, unique=True)
	password = models.CharField(max_length=100, null=True)
	phone = models.CharField(max_length=10, null=True, validators=[MinLengthValidator(10, "Must have strictly 10 digits")])
	rest_name = models.CharField(max_length=50, null=True)
	branch = models.CharField(max_length=50, null=True)
	#user = models.OneToOneField(User, on_delete=models.CASCADE)

	class Meta:
		constraints = [
            models.UniqueConstraint(fields=['branch', 'rest_name'], name='unique seller')
        ]

	def __str__(self):
		return self.rest_name

class Layout(models.Model):
	manager = models.ForeignKey(Manager, on_delete=models.CASCADE)
	name = models.CharField(max_length=50)
	plan = models.CharField(max_length=1000)

	def __str__(self):
		return self.name

class Menu(models.Model):
	manager = models.ForeignKey(Manager, on_delete=models.CASCADE)
	def __str__(self):
		return self.manager.rest_name
	#menudata = models.CharField(max_length=1000)

class FoodItem(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField()
	price = models.DecimalField(max_digits=5, decimal_places=2)
	menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

	def __str__(self):
		return self.name



