from django.conf.urls import url

from django.views.generic.base import RedirectView

from .views import (
    FriendsGetAPIView,
    FriendsAPIView,
)

urlpatterns = [
    # /api/follow/sender_user get receiver_users who are followed by sender_user
    url(r'follow/^(?P<sender_user>[\w.@+-]+', FriendsGetAPIView.as_view(), name='get_follow_list'),
    # /api/follow/sender_user/receiver_user create or delete follow(friends) and return boolean is followed
    url(r'follow/^(?P<sender_user>[\w.@+-]+/^(?P<receiver_user>[\w.@+-]+', FriendsAPIView.as_view(), name='follow'),
]

# ^(?P<username>[\w.@+-]+)/^(?P<username>[\w.@+-]+)/$
