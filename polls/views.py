from multiprocessing import context
from operator import ipow
from re import template
from django.http import Http404
from django.shortcuts import get_object_or_404 , render 
from django.http import HttpResponse
from django.template import loader
from polls.models import Question


def index(request):
    latest_questions_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_questions_list' : latest_questions_list
    }
    # output = ', '.join([q.question_text for q in latest_questions_list])
    # return HttpResponse(template.render(context, request))
    return render(request,'polls/index.html',context)



def detail(request , question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    
    # except Question.DoesNotExist:
    #     raise Http404('Ques DNE')

    # return HttpResponse("you're lookign at que %s" %question_id)
    question = get_object_or_404(Question,pk=question_id)
    return render(request, 'polls/detail.htm',{'question' : question})



def results(request , question_id):
    response = "youre llookijbg at results of quws %s"
    return HttpResponse(response % question_id)




def vote(request , question_id):
    return HttpResponse('youre voting on ques %s' % question_id)


