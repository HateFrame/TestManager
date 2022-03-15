from rest_framework import serializers
from testapp.models import Test, Answer, Question, QuestionChoice, PassedTest


class TestListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Test
        fields = '__all__'


class TestQuestionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = '__all__'

    # def validate(self, attrs):
    #     user = attrs.get('user')
    #     question = attrs.get('question')
    #     selected_answer = attrs.get('answer')


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = '__all__'


class QuestionChoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuestionChoice
        exclude = ('right_choice',)


class CreateAnswerSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Answer
        fields = ['selected_answer', 'user']

    def create(self, validated_data):
        question_object = QuestionChoice.objects.get(id=validated_data.get('selected_answer').id)
        answer_mark = question_object.right_choice
        question = question_object.question
        answer, _ = Answer.objects.update_or_create(
            user=validated_data.get('user'),
            question=question,
            selected_answer=validated_data.get('selected_answer'),
            test=question.test_id,
            right_answer=answer_mark

        )
        return answer

    def validate(self, attrs):
        return attrs


class PassedTestSerializer(serializers.ModelSerializer):

    class Meta:
        model = PassedTest
        fields = ['test']


class TestUserAnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ['question', 'selected_answer', 'right_answer']

