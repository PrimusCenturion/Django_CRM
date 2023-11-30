from django import template

register = template.Library()

@register.inclusion_tag("tags/cookie_popup.html", takes_context=True)
def cookie_preferences_tag(context):
    return {"cookie_preferences": context["cookie_preferences"]}