from django.urls import path
from .views import EvaluatorScoreReview


urlpatterns = [
    path('create_evaluator/', EvaluatorScoreReview.as_view(), name='evaluator')
]