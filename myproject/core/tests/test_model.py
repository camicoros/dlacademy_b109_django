import datetime
import os
import unittest

from django.core.exceptions import ValidationError
from django.test import TestCase

from core.models import CustomUser


class TestCustomUser(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = CustomUser.objects.create(
            username="root",
            password="root",
            avatar=os.path.join("test_media", "01.png")
        )

    def test_future_birth_date(self):
        with self.assertRaises(ValidationError):
            user = CustomUser.objects.get(id=1)
            user.birth_date = datetime.datetime.now() + datetime.timedelta(days=1)
            user.full_clean()
            user.save()

    @unittest.expectedFailure
    def test_past_birth_date(self):
        with self.assertRaises(ValidationError):
            user = CustomUser.objects.get(id=1)
            user.birth_date = datetime.datetime.now() - datetime.timedelta(days=1)
            user.full_clean()
            user.save()


class TestFriends(TestCase):
    @classmethod
    def setUpTestData(cls):
        user1 = CustomUser.objects.create(
            username="root",
            password="root",
            avatar=os.path.join("test_media", "01.png")
        )
        user2 = CustomUser.objects.create(
            username="boot",
            password="boot",
            avatar=os.path.join("test_media", "01.png")
        )

    def test_add_friend(self):
        user1 = CustomUser.objects.get(id=1)
        user2 = CustomUser.objects.get(id=2)
        user1.friends.add(user2)
        self.assertIn(user2, user1.friends.all())
