from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Question, Choice

def index(request):
  # Store 5 question list in desc order by date
  latest_question_list = Question.objects.order_by('-publish_date')[:5]
  # Pass list above to the views as a dictionary
  context = {
    'latest_question_list': latest_question_list
  }
  return render(request, 'polls/index.html', context)

# Show specific question and choices
def detail(request, question_id):
  try:
    question = Question.objects.get(pk=question_id)
  except Question.DoesNotExist:
    raise Http404('Question does not exist')
  return render(request, 'polls/detail.html', { 'question': question })

# Get question and display result
def results(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  return render(request, 'polls/results.html', { 'question': question })

# Vote for a question choice
def vote(request, question_id):
  # print(request.POST['choice'])
  question = get_object_or_404(Question, pk=question_id)
  try:
    selected_choice = question.choice_set.get(pk=request.POST['choice'])
  except (KeyError, Choice.DoesNotExist):
    # Redisplay the question voting form
    return render(request, 'polls/detail.html', {
      'question': question,
      'error_message': 'You didnt select a choice',
    })
  else:
    selected_choice.votes += 1
    selected_choice.save()
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice
    # if user hits the back button
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))