from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Page, Slider

# Apply summernote to all TextField in model.
class PagesAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = ('description', )

admin.site.register(Page, PagesAdmin)

admin.site.register(Slider)
