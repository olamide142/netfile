from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name="smlr")
def smlr(value):
    if(len(value) > 30):
        value = value[0:30]+str("...")
        return value
    else:
        return value


@register.filter(name="tobyte")
def tobyte(value):
    power = 2**10
    n=0
    power_labels = {1:'Kilobytes', 2:'Megabytes', 3:'Gigabytes', 4:'Terabytes'}
    while value > power:
        value /=power
        n +=1
    return str(round(value,1))+" "+ power_labels[n]


