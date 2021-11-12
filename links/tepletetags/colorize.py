from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def colorize(val):
    mark = str(val)[:1]
    if mark=='-':
        html=f"<span style='color:green'{val}></span>"
    elif mark=='0':
        html=f"<span style='color:red'{val}></span>"
    else:
        html=f"<span style='color:yellow'{val}></span>"
    return mark_safe(html)