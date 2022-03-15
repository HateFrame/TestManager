from django.urls import path, include
from .views import (
    TestListView,
    TestQuestionsView,
    QuestionDetailView,
    QuestionChoicesView,
    AnswerCreate,
    PassedTestsView,
    TestUserAnswersView
)
urlpatterns = [
    path('tests/', TestListView.as_view()),
    path('tests/<int:pk>/', TestQuestionsView.as_view()),
    path('tests/question/<int:pk>/', QuestionDetailView.as_view()),
    path('tests/question/<int:pk>/choices/', QuestionChoicesView.as_view()),
    path('tests/answer/', AnswerCreate.as_view()),
    path('tests/passed/', PassedTestsView.as_view()),
    path('tests/<int:test_id>/answers', TestUserAnswersView.as_view())
]