from django.test import TestCase, Client
import datetime
from django.utils import timezone
from django.urls import reverse
from .models import Student
class TestGrade(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse("testmania:grade")
class TestGradeConversion(TestCase):
    
    def test_five_to_six(self):
        data = {
            "input_grade" : 5
        }
        response = self.client.get(self.url, data)

        self.assertContains(response, 6)
        
class TestElementary(TestCase):

    def test_real_elementary(self):
        elem = "천전"
        not_elem = Student(elementary=elem)
        self.assertIs(not_elem.is_real_elementary(), False)


# Create your tests here.
