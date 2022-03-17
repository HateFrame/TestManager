from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Test(models.Model):
    title = models.CharField(max_length=2048, verbose_name='Название теста')
    count = models.PositiveSmallIntegerField(verbose_name='Количество вопросов')

    def __str__(self):
        return self.title


class Question(models.Model):
    title = models.TextField(max_length=4096, verbose_name='Вопрос')
    test = models.ForeignKey(Test, on_delete=models.PROTECT)

    ONE = 'radio'
    MULTIPLE = 'checkbox'
    TEXT = 'text'

    QUESTION_TYPES = (
        (ONE, 'Один ответ'),
        (MULTIPLE, 'Несколько ответов'),
        (TEXT, 'Текстовый ответ')
    )

    question_type = models.CharField(choices=QUESTION_TYPES, default=ONE, max_length=128)

    def __str__(self):
        return self.title


class QuestionChoice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.PROTECT)
    answer_variable = models.TextField(max_length=2048, verbose_name='Вариант ответа')
    right_choice = models.BooleanField(default=False, verbose_name='Верный вариант ответа')

    def __str__(self):
        return f'{self.answer_variable} {self.question}'


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    question = models.ForeignKey(Question, on_delete=models.PROTECT)
    selected_answer = models.ForeignKey(QuestionChoice, on_delete=models.PROTECT)
    test = models.ForeignKey(Test, on_delete=models.PROTECT, default=1)
    right_answer = models.BooleanField(verbose_name='Ответ верный')
    text = models.TextField(blank=True, null=True, default='')

    def __str__(self):
        return f'{self.user}|{self.question}'


class PassedTest(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    test = models.ForeignKey(Test, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.user}|{self.test}'
