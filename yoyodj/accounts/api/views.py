from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import F
from django.db.models import Q
from rest_framework import permissions
from .serializers import UsersSerializer, FriendsSerializer
from ..models import Users, Friends
import requests

# TO DO : include permissions and get current user by middleware setting / include userapiview in toggle_follow

# requests get access token api url and get access token data
def get_current_idx(api_uri):
    uri_data = requests.get(api_uri)
    json_data = uri_data.json()
    user_idx = json_data['idx']
    return user_idx


'''
Request parameters are the result of submitting an HTTP request with a query string that specifies the name/value
pairs, or of submitting an HTML form that specifies the name/value pairs. ... For example, when you do a post
from html, data can be automatically retrieved by using request.
'''

'''
UserAPIView's get function return current profile page's user's info
'''
class UserAPIView(APIView):
    def get(self, request, user_id, format=None):
        if request.method == 'GET':
            renderer_classes = [JSONRenderer]
            # username in url is user_id prams and profile_user is a object
            profile_user = Users.objects.filter(user_id=user_id)
            serializer = UsersSerializer(profile_user, many=True)
            return Response(serializer.data)
    # serializer.data result
    # [
    #  {'idx' : 0, 'user_id' : "something", ... }, {'idx' : 1, 'user_id' : "sth2", ..}, ...
    # ]
'''
# FriendsGetAPIView's function: return sender user's following friends objects by json 
# and sender user is post(==profile) user
'''
class FriendsGetAPIView(APIView):
    def get_list(self, request, sender_user, format=None):
        if request.method == 'GET':
            renderer_classes = [JSONRenderer]
            su_qs = Users.objects.get(user_id=F(sender_user))
            sender_user_idx = su_qs['idx']
            '''
            # get current profile_user's following users idx by list
            '''
            following_users_list = Friends.objects.get_following(sender_user_idx)
            following_users_obj = Users.objects.filter(idx__in=following_users_list)
            serializer = FriendsSerializer(following_users_obj, many=True)
            return Response(serializer.data)

class FriendsAPIView(APIView):

    # return added(True or False) by json
    def toggle_follow(self, request, sender_user, receiver_user, format=None):
        if request.method == 'POST':
            # data is Friends object by json
            # toggle_follow = Friends.objects.toggle_follow(data['sender_idx'], data['receiver_idx'])

            # get sender_user's idx
            su_qs = Users.objects.get(user_id=F(sender_user))
            sender_user_idx = su_qs['idx']
            # get receiver_user's idx
            ru_qs = Users.objects.get(user_id=F(receiver_user))
            receiver_user_idx = ru_qs['idx']
            # objects.toggle_follow function return False if unfollow, True if following
            toggle_follow = Friends.objects.toggle_follow(sender_user_idx, receiver_user_idx)
            return Response({'added': toggle_follow})
            # or
            # serializer = toggle_follow.json()
            # return Response(serializer.data)
#             is follow is false -> unfollow & is follow is true -> following

    '''
    get boolean type value: True-> sender user is following, False-> user isn't following
    '''
    def get_am_i_following(self, request, sender_user, receiver_user, format=None):
        if request.method == 'GET':
            su_qs = Users.objects.get(user_id=F(sender_user))
            sender_user_idx = su_qs['idx']
            ru_qs = Users.objects.get(user_id=F(receiver_user))
            receiver_user_idx = ru_qs['idx']

            # sender_idx == current user
            is_follow = Friends.objects.is_follow(sender_user_idx, receiver_user_idx)
            return Response({'followed': is_follow})
            # serializer = is_follow.json()
            # return Response(serializer.data)
            # current_user_idx = get_current_idx(api_uri)
            # i_following_obj = Friends.objects.filter(Q(sender_idx=F(current_user_idx)) & Q(receiver_idx=F(receive_users)))
            # serializer = FriendsSerializer(i_following_obj, many=True)
            # return Response(serializer.data)
