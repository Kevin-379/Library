from django import template

register = template.Library()


@register.filter(name='has_group')
def has_group(value, arg):
	for group in value.groups.all():
		if group.name == arg:
			return True
	return False
