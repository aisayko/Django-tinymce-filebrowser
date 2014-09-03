from django.conf import settings
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse
from django.contrib.admin.views.decorators import staff_member_required

from mce_filebrowser.models import FileBrowserFile
from mce_filebrowser.forms import FileUploadForm
from mce_filebrowser.utils import render_paginate


@staff_member_required
def filebrowser(request, file_type):
    """ Trigger view for filebrowser """
    template = 'filebrowser.html'
    upload_form = FileUploadForm()
    uploaded_file = None
    upload_tab_active = False
    is_images_dialog = (file_type == 'img')
    is_documents_dialog = (file_type == 'doc')
    
    files = FileBrowserFile.objects.filter(file_type=file_type)
    
    if request.POST:
        upload_form = FileUploadForm(request.POST, request.FILES)
        upload_tab_active = True
        
        if upload_form.is_valid():
            uploaded_file = upload_form.save(commit=False)
            uploaded_file.file_type = file_type
            uploaded_file.save()
    
    data = {
        'upload_form': upload_form,
        'uploaded_file': uploaded_file,
        'upload_tab_active': upload_tab_active,
        'is_images_dialog': is_images_dialog,
        'is_documents_dialog': is_documents_dialog
    }
    per_page = getattr(settings, 'FILEBROWSER_PER_PAGE', 20)
    return render_paginate(request, template, files, per_page, data)


@staff_member_required
def filebrowser_remove_file(request, item_id, file_type):
    """ Remove file """
    fobj = get_object_or_404(FileBrowserFile, file_type=file_type, id=item_id)
    fobj.delete()
    
    if file_type == 'doc':
        return HttpResponseRedirect(reverse('mce-filebrowser-documents'))
    
    return HttpResponseRedirect(reverse('mce-filebrowser-images'))
