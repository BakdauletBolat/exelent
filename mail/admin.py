from django.contrib import admin
from .models import Mail, TypeSeminar
# Register your models here.


class MailAdmin(admin.ModelAdmin):
    model = Mail
    search_fields = ['name', 'phone','email']
    list_filter = ('typeSeminar',)
    list_display = ('surname','lastname','name','phone','email','universityjob','position','consent','typeSeminar')

admin.site.register(Mail,MailAdmin)
admin.site.register(TypeSeminar)