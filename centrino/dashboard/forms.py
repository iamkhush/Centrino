from django import forms

class dashboard(forms.Form):
	csv = forms.FileField()
