from rest_framework import viewsets

from profiles.models import UserProfile
from profiles.serializers import UserProfileSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


userprofile_list = UserProfileViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

userprofile_detail = UserProfileViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
