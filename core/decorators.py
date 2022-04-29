from django.http import HttpResponse
from django.shortcuts import redirect


def anonymous_user_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func


def allowed_groups(allowed_groups=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_groups:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("You are not AUTHORIZED to view this page!", status = 401)
        return wrapper_func
    return decorator
