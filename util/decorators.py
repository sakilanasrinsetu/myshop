from django.contrib.auth.decorators import login_required, user_passes_test
from django.conf import settings


# Has Permission Checker

user_has_permission = user_passes_test(
    lambda user: user.has_perm('') == True, login_url=settings.ACCESS_DENIED_URL
)


def has_permission_required(view_func):
    decorated_view_func = login_required(user_has_permission(view_func))
    return decorated_view_func


# has dashboard permission required


has_dashboard_permission = user_passes_test(
    lambda user: user.is_superuser == True or not user.user_profile.created_by == None, login_url=settings.HOME_URL
)


def has_dashboard_permission_required(view_func):
    decorated_view_func = login_required(has_dashboard_permission(view_func))
    return decorated_view_func