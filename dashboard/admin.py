from django.contrib import admin

from .models import Lead
from .forms import LeadCreationForm

class LeadAdmin(admin.ModelAdmin):
    form = LeadCreationForm
    list_display = ('title', 'first_name', 'last_name',)
    search_fields = ('first_name','email', )
    list_filter = ('title',)
    #  TODO Finish this fieldset to include all the relevant data and 
    #  relevant headings
    fieldsets = [
        (
            "Basic Information",
            {
                "fields": [
                    'title', 'first_name', 'last_name',
                    'email','phone_number', 'mobile_number'
                    ],
            },
        ),
        (
            "Advanced options",
            {
                "classes": ["collapse"],
                "fields": [],
            },
        ),
    ]

admin.site.register(Lead, LeadAdmin)
