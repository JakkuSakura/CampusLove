from django.http import HttpResponse
from users.models import User

from utils.permissions_table import positive, passive, create_permissions, PERMISSIONS_TABLE


def perm_check(action: str, nowuser: User = None, user: User = None):
    return PERMISSIONS_TABLE.getPermsDict(user.userprofile)[passive(action)] and \
           PERMISSIONS_TABLE.getPermsDict(nowuser.userprofile)[positive(action)]


def check_permission(func, action: str, nowuser: User = None, user: User = None):
    def wrapper(*args, **kwargs):
        if not perm_check(action, nowuser, user):
            return HttpResponse(403, "Do not have permissions")
        return func(*args, **kwargs)

    return wrapper

