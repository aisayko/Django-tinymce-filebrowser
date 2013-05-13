django-tinymce-filebrowser
===

**django-tinymce-filebrowser** is a simple and flexible tool for managing your files and images from TinyMCE editor.

Quickstart:
===

Install django-tinymce-filebrowser:

    $ pip install django-tinymce-filebrowser

Add tinymce and mce_filebrowser to INSTALLED_APPS in settings.py for your project:

    INSTALLED_APPS = (
        ...
        'tinymce',
        'mce_filebrowser',
    )
    
Change tinymce config to work with filebrowser:

    TINYMCE_DEFAULT_CONFIG = {
      'file_browser_callback': 'mce_filebrowser'
    }

Add mce_filebrowser.urls to urls.py for your project:

    urlpatterns = patterns('',
        ...
        (r'^tinymce/', include('tinymce.urls')),
        (r'^mce_filebrowser/', include('mce_filebrowser.urls')),
    )

In your models.py code:

    from django.db import models
    from tinymce.models import HTMLField

    class MyModel(models.Model):
        ...
        content = HTMLField()
        
In your admin.py:

    from django.contrib import admin
    from myapp.models import MyModel
    from mce_filebrowser.admin import MCEFilebrowserAdmin

    class MyModelAdmin(MCEFilebrowserAdmin):
        pass

    admin.site.register(MyModel, MyModelAdmin)

**django-tinymce-filebrowser** uses django staticfiles.


If You do not use django-tinymce package then add next lines to TinyMCE init:

    tinyMCE.init({
        ...
        "file_browser_callback": "mce_filebrowser"
    })
