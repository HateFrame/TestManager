from django.contrib import admin
from django.forms import Textarea
from django.db import models
from testapp.models import Test, Question, QuestionChoice, Answer, PassedTest

import nested_admin


class QuestionChoiceInline(nested_admin.NestedTabularInline):
    model = QuestionChoice
    extra = 2
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 2, 'cols': 60})},
    }


class QuestionInline(nested_admin.NestedTabularInline):
    model = Question
    inlines = [QuestionChoiceInline]
    extra = 1
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 3, 'cols': 60})},
    }


class TestAdmin(nested_admin.NestedModelAdmin):
    inlines = [QuestionInline]


admin.site.register(Test, TestAdmin)
admin.site.register(Question)
admin.site.register(QuestionChoice)
admin.site.register(Answer)
admin.site.register(PassedTest)
