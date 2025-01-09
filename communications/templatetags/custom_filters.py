from django import template

register = template.Library()

@register.filter
def format_phone(value):
    """
    Formatea un número de teléfono en el formato +56 9 xxxx xxxx.
    """
    if len(value) == 12 and value.startswith("+56"):
        return f"{value[:3]} {value[3]} {value[4:8]} {value[8:]}"
    return value