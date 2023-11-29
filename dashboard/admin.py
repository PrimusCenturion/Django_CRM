from django.contrib import admin

from .models import Lead, SocialMediaLink, StreetAddressZA
from .forms import LeadCreationForm

class SocialMediaLinksInline(admin.TabularInline):
    model       = SocialMediaLink
    classes     = ["collapse"]
    extra       = 1

class StreetAddressZAInline(admin.StackedInline):
    model       = StreetAddressZA
    classes     = ["collapse"]
    extra       = 1

@admin.display(description="Full Name")
def upper_case_name(obj):
    return f"{obj.first_name}, {obj.last_name}".upper()

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    form                = LeadCreationForm
    list_display        = (upper_case_name, 'title',)
    search_fields       = ('first_name','email', )
    list_filter         = ('title',)

    filter_horizontal = ('social_media_links',)

    #  TODO Finish this fieldset to include all the relevant data and 
    #  relevant headings
    fieldsets = [
        (
            "Basic Information",
            {
                "fields": [
                    'title', 'first_name', 'last_name',
                    'email','phone_number', 'mobile_number',
                    'personal_website'
                    ],
                "description":""
            },
        ),
        (
            "Professional Information",
            {
                "classes":['collapse'],
                "fields":[
                    'job_title', 'company_name', 
                    'company_website',
                    ],
            }
        ),
        (
            "Advanced options",
            {
                "classes": ["collapse"],
                "fields": [],
            },
        ),
    ]

    inlines = [
        SocialMediaLinksInline, 
        StreetAddressZAInline
    ]

@admin.register(StreetAddressZA)
class StreetAddressZAAdmin(admin.ModelAdmin):
    readonly_fields = ["full"]

# @admin.register(SocialMediaLink)
# class SocialMediaLinksAdmin(admin.ModelAdmin):
#     list_display        = ('prospect','social_media', 'link')
#     search_fields       = ('lead__first_name','lead__last_name')
#     list_filter         = ('social_media',)

