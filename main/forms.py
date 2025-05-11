from django import forms
from .models import Files

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = Files
        fields = ('file_name', 'file_file')