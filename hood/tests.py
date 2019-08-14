from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserProfile,Post,Comment,Neighborhood,Company
# Create your tests here.
class UserProfileTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.profile = UserProfile(id=1,first_name='John',last_name='Doe',user = self.user,bio='test bio')

    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.profile,UserProfile))

class PostTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.post = Post(id=1,title='Test',content='This is a test',user = self.user)

    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.post,Post))

