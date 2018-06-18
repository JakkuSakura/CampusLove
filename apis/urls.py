from django.conf.urls import include
from django.urls import path
from rest_framework import routers

# from profiles.views import UserProfileViewSet
from snippets.views import SnippetViewSet

router = routers.DefaultRouter()

router.register('snippets', SnippetViewSet)
# router.register('userprofiles', UserProfileViewSet)
# api url 配置
urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),

]