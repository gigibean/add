from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.
from .models import Users, Friends

User = get_user_model()


class UsersTestCase(TestCase):
    def setUp(self):
        self.nickname = "some_user"
        self.id = "user"
        new_user = User.objects.create(nickname=self.nickname, id=self.id)

    def test_profile_created(self):
        nickname = self.nickname
        user_profile = Users.objects.filter(user_nickname=self.nickname)
        self.assertTrue(user_profile.exists())
        self.assertTrue(user_profile.count() == 1)

    def test_new_user(self):
        new_user = User.objects.create(nickname=self.nickname + "abcsd")
