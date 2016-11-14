from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import Question, Choice


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    # By default rails recognizes the lower-cased version of the Model as object in specified view
    # In this case because its a list view, the default is question_list
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Returns the last 5 published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    # By default rails recognizes the lower-cased version of the Model as object in specified view
    # To override name, use context_object_name = 'name_to_use_instead'
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    # By default rails recognizes the lower-cased version of the Model as object in specified view
    # To override name, use context_object_name = 'name_to_use_instead'
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form
        context = {
            'question': question,
            'error_message': 'You did\'nt Select a choice',
        }
        return render(request, 'polls/detail.html', context)
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))




