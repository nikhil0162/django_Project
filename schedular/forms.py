from django import forms


class EmailSendForm(forms.Form):
	subject = forms.CharField(max_length=50)
	message = forms.Textarea()
	send_by = forms.EmailField(required=True)