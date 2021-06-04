from polls.models import Question
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader

def index(request):
    ultimas_enquetes = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'ultimas_enquetes': ultimas_enquetes,
    }
    return HttpResponse(template.render(context, request))

def detail (request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("A enquete não existe")
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)