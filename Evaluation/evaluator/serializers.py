from .models import Evaluator
from rest_framework import serializers


class EvaluatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluator
        fields = ['id', 'name', 'title', 'candidate', 'scores', 'comment', 'time_created']
        