from django import forms
from .models import CarPost
from django_bleach.forms import BleachField
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput


class CarForm(forms.ModelForm):
	# gender = forms.BooleanField(disabled=True)
	class Meta:
		model = CarPost
		fields = ['company_name', 'model_name', 'image', 'launched_date', 'gender', 'description', 'company_contact_no']
		widgets = {	
			'company_name': forms.TextInput(attrs={'id': 'company_name'}),
			'model_name': forms.TextInput(attrs={'id': 'model_name'}),
			'image': forms.FileInput(attrs={'id': 'car_upload'}),
			# 'launched_date': forms.DateInput(attrs={'type': 'date', 'id': 'launch_date'}),
			'launched_date': DateTimePickerInput(attrs={'id': 'launched_date'}),

		}
	# company_name = BleachField()
	# model_name = BleachField()

	# import re
	# def clean_company_name(self):
	# 	company_name = self.cleaned_data['company_name']
	# 	# pattern = re.compile('\\W')
	# 	if all(x.isalpha() or x.isspace() for x in company_name):
	# 		print("ok")
	# 		return company_name
	# 		# raise forms.ValidationError("Please use only alphabet characters!!!")
	# 	else:
	# 		print("not ok")
	# 		raise forms.ValidationError("Please use only alphabet characters!!!")


class CarUpdateForm(forms.ModelForm):
	class Meta:
		model = CarPost
		fields = ['company_name', 'model_name', 'image', 'launched_date', 'description', 'company_contact_no']