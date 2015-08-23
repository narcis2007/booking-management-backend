from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Question
from .serializers import QuestionSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionListView(APIView):
    queryset = Question.objects.all()

    def get(self, request, format=None):
        questions = []
        for question in Question.objects.all():
            serilizer = QuestionSerializer(
                question, context={'request': request})
            questions.append(serilizer.data)
        return Response(questions)

