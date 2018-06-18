from django.contrib import admin
from users.admin import UserAdmin
from users.models import User

from profiles.models import UserProfile


class ProfileInline(admin.StackedInline):
    model = UserProfile
    max_num = 1
    can_delete = False


class UserProfileAdmin(UserAdmin):
    inlines = [ProfileInline, ]


admin.site.unregister(User)
admin.site.register(User, UserProfileAdmin)