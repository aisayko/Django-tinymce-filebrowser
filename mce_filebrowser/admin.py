from django.contrib import admin


class MCEFilebrowserAdmin(admin.ModelAdmin):
  
  class Media:
      js = ('mce_filebrowser/js/filebrowser_init.js',)
