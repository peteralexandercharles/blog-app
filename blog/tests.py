from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Post

class BlogTests(TestCase):
    
    def setUp(self):
        """Setup a test user and a test post"""
        self.user = get_user_model().objects.create_user(
                username='testuser',
                email='test@email.com',
                password='secret',
                )
        self.post = Post.objects.create(
                title='A good title',
                body='Nice body content',
                author=self.user,
                )
        self.second_post = Post.objects.create(
                title='second title post',
                body='body text',
                author=self.user,
                )

    def test_string_representation(self):
        object = Post(title='A sample title')
        self.assertEqual(str(object), object.title)

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', "A good title")
        self.assertEqual(f'{self.post.body}', 'Nice body content')
        self.assertEqual(f'{self.post.author}', f'{self.user.username}')
        self.assertEqual(f'{self.post.author}', 'testuser')

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'second title post')
        self.assertContains(response, f'{self.post.body}')
        self.assertContains(response, f'Nice body content')
        self.assertTemplateUsed(response, 'home.html')

    def test_post_detail_view(self):
        response = self.client.get('/post/1/')
        response_2 = self.client.get('/post/2/')
        no_response = self.client.get('/post/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_2.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A good title')
        self.assertContains(response_2, 'second title post')
        self.assertTemplateUsed(response, 'post_detail.html')
        self.assertTemplateUsed(response_2, 'post_detail.html')


