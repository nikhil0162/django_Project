from django import forms
from .models import CarPost

class CarForm(forms.ModelForm):
	class Meta:
		model = CarPost
		fields = ['company_name', 'model_name', 'image', 'launched_date']