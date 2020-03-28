from django import forms

class UploadFileForm(forms.Form):
    owner = forms.CharField(max_length=50)
    file = forms.FileField()