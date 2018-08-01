from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("this is first index view")

def detail(request, question_id):
    return HttpResponse("you are looking at question {}".format(question_id))

def results(request, question_id):
    response = "this page shows reults of question {}"
    return HttpResponse(response.format(question_id))
    
def vote(request, question_id):
    return HttpResponse("votes of question {}".format(question_id))
   