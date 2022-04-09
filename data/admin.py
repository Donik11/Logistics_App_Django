from django.contrib import admin

from .forms import DataForm
from .models import Data


from django.contrib.auth.models import Group
from django.contrib.auth.models import User

admin.site.unregister(Group)
admin.site.unregister(User)
@admin.register(Data)
class DataAdmin(admin.ModelAdmin):
    list_display = ("id", "fio","carnumber","regdata","tirnumber","waybill","cmr1","cmr2","dazvol","tc","tircheck","waybillcheck","cmr1check","cmr2check","dcheck","tcheck","checker")
    form = DataForm

