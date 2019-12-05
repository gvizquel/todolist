
"""
"""
# Django Libraries
from django import template

register = template.Library()


@register.filter
def get_obj_attr(obj, attr):
    return getattr(obj, attr)


@register.filter(name='has_group')
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists()


@register.filter(name='url_target_blank', is_safe=True)
def url_target_blank(text):
    return text.replace('<a ', '<a target="_blank" ')
