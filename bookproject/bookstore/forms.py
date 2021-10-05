from django import forms
from .models import store

class storeForm(forms.ModelForm):
	class Meta:
		model=store
		fields="__all__"

		widgets = {
		'bookname':forms.TextInput(attrs={'class':'form-control'}),
		'releasedate':forms.DateInput(attrs={'class':'form-control','id':'datepicker'}),#datepicker is interesting feature using with the help of jquery..
		'about':forms.TextInput(attrs={'class':'form-control'})

		}