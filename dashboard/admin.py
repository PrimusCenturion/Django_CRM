from django.contrib import admin

from .models import Lead
from .forms import LeadCreationForm

class LeadAdmin(admin.ModelAdmin):
    form = LeadCreationForm

admin.site.register(Lead, LeadAdmin)
