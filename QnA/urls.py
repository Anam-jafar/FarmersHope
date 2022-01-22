from django.urls import path, include
from . import views
from .views import QuestionListView, QuestionCreateView

urlpatterns = [
    path('', QuestionListView.as_view(), name='qna-dashboard'),
    path('add_question/', QuestionCreateView.as_view(), name='question'),
    path('question/<int:pk>', views.questionAnswerDetail, name='qna-detail')
]
