import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Question

def create_question(question_text, days):
    """
    과거에 발행된 질문들에 대해서 negative, 아직 발행되지 않은 질문들에 대해서 positive
    """
    time = timezone.now() + datetime.timedelta(days = days)
    return Question.objects.create(question_text = question_text, pub_date = time)

class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):

        time = timezone.now() + datetime.timedelta(days = 30)
        future_question = Question(pub_date = time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        time = timezone.now() - datetime.timedelta(days = 1, seconds = 1)
        old_question = Question(pub_date = time)
        self.assertIs(old_question.was_published_recently(), False)
    
    def test_was_published_recently_with_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours = 23, minutes = 59, seconds = 59)
        recent_question = Question(pub_date = time)
        self.assertIs(recent_question.was_published_recently(), True)
    
class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        """
        질문이 존재하지 않는다면, 적절한 메세지가 나타난다.
        """
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_past_question(self):
        """
        과거 질문은 인덱스 페이지에 나타납니다.
        """
        create_question(question_text = "Past question.", days = -30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question.>']
        )
    
    def test_future_question(self):
        """
        미래 질문은 인덱스 페이지에서 나타나지 않습니다.
        """
        create_question(question_text = "Future question.", days = 30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_future_question_and_past_question(self):
        """
        과거와 미래의 질문이 존재한다고 하더라도, 오직 과거 질문만 나타냅니다.
        """
        create_question(question_text = "Past question.", days = -30)
        create_question(question_text = "Future question.", days = 30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question.>']
        )

    def test_two_past_questions(self):
        """
        질문들이 있는 인덱스 페이지가 여러 개의 질문들을 나타냅니다.
        """
        create_question(question_text = "Past question 1.", days = -30)
        create_question(question_text = "Past question 2.", days = -5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question 2.>', '<Question: Past question 1.>']
        )
class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        """
        미래에 발행된 질문에 대한 view는 404에러 return
        """
        future_question = create_question(question_text = 'Future question.', days = 5)
        url = reverse("polls:detail", args = (future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        """
        과거에 발행된 질문에 대한 view는 나타난다.
        """
        past_question = create_question(question_text = "Past Question.", days = -5)
        url = reverse('polls:detail', args = (past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)

# Create your tests here.
