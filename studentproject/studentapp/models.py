from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# from phonenumber_field import formfields
import phonenumbers


class studentinfo(models.Model):
	profile_pic=models.ImageField(upload_to='studentphotos')
	name=models.CharField(max_length=50)
	bio=models.TextField()
	contact=PhoneNumberField()
	address=models.CharField(max_length=50)
	email=models.EmailField()

	def __str__(self):
		return self.name

