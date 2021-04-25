def admin_required(func):
	def wrapper(request, *args, **kwargs):
		if request.user.groups.exists():
			for group in request.user.groups.all():
				print(group.name)
		return func(request, *args, **kwargs)
	return wrapper
