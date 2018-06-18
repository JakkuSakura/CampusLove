from django.contrib import admin

import xadmin
from snippets.models import Snippet

admin.site.register(Snippet)
xadmin.site.register(Snippet)