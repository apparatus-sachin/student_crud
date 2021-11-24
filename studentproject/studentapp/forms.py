from django import forms
from .models import *
# from phonenumber_field import formfields
# import phonenumbers
class studentinfoForm(forms.ModelForm):
	class Meta:
		model = studentinfo
		fields ="__all__"

		widgets={
		'name':forms.TextInput(attrs={'class':'form-control'}),
		'bio':forms.Textarea(attrs={'rows':5,'cols':90,'style':'height:1em;'}),
		# 'contact':forms.TextInput(attrs={'placeholder': _('phone')}),
		'address':forms.TextInput(attrs={'class':'form-control'}),
		'email':forms.EmailInput(attrs={'class':'form-control'})
		}