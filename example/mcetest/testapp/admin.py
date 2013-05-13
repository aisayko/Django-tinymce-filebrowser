from django.contrib import admin
from testapp.models import MCETest
from mce_filebrowser.admin import MCEFilebrowserAdmin


class MCETestAdmin(MCEFilebrowserAdmin):
    pass


admin.site.register(MCETest, MCETestAdmin)
