from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

from django.contrib.auth.models import User
from django_filters import rest_framework as filters
from testapp.models import Test, Question, QuestionChoice, PassedTest, Answer
from testapp.serializers import (
    TestListSerializer,
    TestQuestionsSerializer,
    QuestionSerializer,
    QuestionChoiceSerializer,
    CreateAnswerSerializer,
    PassedTestSerializer,
    TestUserAnswerSerializer,
    CreatePassedTestSerializer,
    PassedTestUserSerializer
)


class TestListView(generics.ListAPIView):
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]
    queryset = Test.objects.all()
    serializer_class = TestListSerializer


class TestQuestionsView(generics.ListAPIView):
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]
    serializer_class = TestQuestionsSerializer

    def get_queryset(self):
        test_id = self.kwargs['pk']
        return Question.objects.filter(test=test_id)


class QuestionDetailView(generics.RetrieveAPIView):
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionChoicesView(generics.ListAPIView):
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]
    serializer_class = QuestionChoiceSerializer

    def get_queryset(self):
        question_id = self.kwargs['pk']
        return QuestionChoice.objects.filter(question=question_id)


class AnswerCreate(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CreateAnswerSerializer


class PassedTestsView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PassedTestSerializer

    def get_queryset(self):
        return PassedTest.objects.filter(user=self.request.user)


class TestUserAnswersView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TestUserAnswerSerializer

    def get_queryset(self):
        test_id = self.kwargs['test_id']
        return Answer.objects.filter(user=self.request.user, test=test_id)


class PassedTestsCreate(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CreatePassedTestSerializer


class UserFilter(filters.FilterSet):

    class Meta:
        model = PassedTest
        fields = ['user', 'test']


class UserListView(generics.ListAPIView):
    # permission_classes = [IsAdminUser]
    permission_classes = [AllowAny]
    queryset = PassedTest.objects.all()
    serializer_class = PassedTestUserSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = UserFilter
