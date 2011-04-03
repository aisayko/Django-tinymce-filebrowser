from django.conf.urls.defaults import *

from mce_filebrowser import views


urlpatterns = patterns('',
    url(r'^image/$', 
        views.filebrowser, 
        {'file_type': 'img'},
        name='mce-filebrowser-images'
    ),
    url(r'^file/$', 
        views.filebrowser, 
        {'file_type': 'doc'},
        name='mce-filebrowser-documents'
    ),
    url(r'^image/remove/(?P<item_id>\d+)/$', 
        views.filebrowser_remove_file, 
        {'file_type': 'img'},
        name='mce-filebrowser-remove-image'
    ),
    url(r'^file/remove/(?P<item_id>\d+)/$', 
        views.filebrowser_remove_file, 
        {'file_type': 'doc'},
        name='mce-filebrowser-remove-document'
    )
)