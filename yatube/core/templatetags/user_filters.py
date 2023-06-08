from django import template
register=template.Library()

@register.filter
def addclass(field,css):
    return field.as_widget(attrs={'class':css})

@register.filter
def uglify(t):
    v=""
    for s,d in enumerate(t):
        if s%2!=0:
            d=d.lower()
            v+=d
        if s%2==0:
            d=d.upper()
            v+=d
    return v
