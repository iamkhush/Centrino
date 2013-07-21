from django import forms

class dashboard(forms.Form):
	csv = forms.FileField()

class flexitest(forms.Form):
	name = forms.CharField(max_length=30)
	age = forms.IntegerField()
	email = forms.EmailField()