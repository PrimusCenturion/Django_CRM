import logging
logger = logging.getLogger(__name__)

from django.test import TestCase
from django.urls import reverse

class TestHomeView(TestCase):
    
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_page_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'pages/home.html')

    def test_home_page_template_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'pages/home.html')

    def test_home_page_title_content(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response.content, "<html>")

