from django.http import HttpResponse


def index(request):
    return HttpResponse("Index page")


def detail(request, question_id):
    return HttpResponse("you are looking at the details of " + str(question_id))


def results(request, question_id):
    return HttpResponse("you are looking at the results of " + str(question_id))


def vote(request, question_id):
    return HttpResponse("you are looking at the vote of " + str(question_id))