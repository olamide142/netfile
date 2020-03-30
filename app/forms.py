from django import forms

class UploadFileForm(forms.Form):
    filesize = forms.CharField(max_length=99)
    file_extension = forms.CharField(max_length=10)
    file_name = forms.CharField(max_length=250)
    file = forms.FileField()