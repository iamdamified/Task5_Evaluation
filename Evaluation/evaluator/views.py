from django.shortcuts import render
from .models import Evaluator
from .serializers import EvaluatorSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class EvaluatorScoreReview(ListCreateAPIView):
    queryset = Evaluator.objects.all()
    serializer_class = EvaluatorSerializer
    # permission_classes = (IsAuthenticated) # We may add permission if necessary.
