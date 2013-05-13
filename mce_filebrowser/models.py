from django.db import models
from django.utils.translation import ugettext as _


class FileBrowserFile(models.Model):
    """ Uploaded file model """
    FILE_TYPES = (
        ('img', _('Image')),
        ('doc', _('Document')),
    )
    
    file_type = models.CharField(max_length=3, choices=FILE_TYPES)
    uploaded_file = models.FileField(
        upload_to='mce_filebrowser/%Y/%m/%d',
        verbose_name = _('File / Image')
    )
    create_date = models.DateTimeField(
        auto_now_add=True, verbose_name=_('Create date')
    )
    
    def __unicode__(self):
        return u'%s' % self.uploaded_file.name
