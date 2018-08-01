from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Question

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list' : latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    return HttpResponse("you are looking at question {}".format(question_id))

def results(request, question_id):
    response = "this page shows reults of question {}"
    return HttpResponse(response.format(question_id))
    
def vote(request, question_id):
    return HttpResponse("votes of question {}".format(question_id))
   