from django.contrib import admin

from .models import Lead
from .forms import LeadCreationForm

class LeadAdmin(admin.ModelAdmin):
    form = LeadCreationForm
    list_display = ('title', 'first_name', 'last_name',)
    search_fields = ('first_name','email', )
    list_filter = ('title',)

admin.site.register(Lead, LeadAdmin)
