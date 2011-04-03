from django import forms

from mce_filebrowser.models import FileBrowserFile


class FileUploadForm(forms.ModelForm):
    """ Docstring """
    class Meta:
        model = FileBrowserFile
        fields = ('uploaded_file',)
