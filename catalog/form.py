from django import forms
from catalog.models import Image

class ImageForm(forms.ModelForm):
	class Meta:
		model = Image
		fields = ('name', 'desc', 'date', 'img',)
