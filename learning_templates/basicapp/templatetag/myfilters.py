from django import template

register = template.Library()
@register.filter
def rtx(value,arg):
    """""
    This cuts out all value of 'arg' from the string
    """""
    return value.replace(arg,'')

# register.filter('cut',cut)
