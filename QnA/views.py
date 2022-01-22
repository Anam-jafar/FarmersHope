from django.shortcuts import render, redirect
from .models import Question, Response
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import QuestionDetailForm, ResponseForm


def qnaDashboard(request):
    return render(request, 'QnA/qnaDashboard.html')


class QuestionListView(ListView):
    model = Question
    context_object_name = 'questions'


class QuestionCreateView(LoginRequiredMixin, CreateView):
    model = Question
    fields = ['title', 'body', 'img', 'video']
    success_url = '/qna_dashboard/'

    # for create and update
    # <app>/<model>_form.html
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def questionAnswerDetail(request, pk):
    response_form = ResponseForm
    question = Question.objects.get(pk=pk)
    if request.method == 'POST':
        try:
            response_form = ResponseForm(request.POST)
            if response_form.is_valid():
                response = response_form.save(commit=False)
                response.user = request.user
                response.question = Question(pk=pk)
                response.save()
                return redirect(request.path)
        except Exception as e:
            print(e)
            raise

    context = {
        'question': question,
        'response_form': response_form
    }
    return render(request, 'QnA/qnaDetail.html', context)
