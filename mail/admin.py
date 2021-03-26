from django.contrib import admin
from .models import Mail
# Register your models here.


class MailAdmin(admin.ModelAdmin):
    model = Mail
    search_fields = ['name', 'phone','email']
    list_display = ('surname','lastname','name','phone','email','universityjob','position','consent')

admin.site.register(Mail,MailAdmin)