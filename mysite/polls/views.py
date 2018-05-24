from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Question
def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	#output = ', '.join([q.question_textfor q in latest_question_list])
	template = loader.get_template('polls/index.html')
	context = {
		'latest_question_list': latest_question_list,
	}
	return HttpResponse(template.render(context, request))
# Create your views here.
def detail(request, question_id):
	#try:
	#	question = Question.objects.get(pk=question_id)
	#except:
	#	raise Http404("Question does not exist")
	question = get_object_or_404(Question, pk=question_id)

	return HttpResponse("You're looking at the question {}.".format(question_id))

def results(request, question_id):
	return HttpResponse("You're looking at the results of question {}.".format(question_id))

def vote(request, question_id):
	return HttpResponse("You're voting on question {}.".format(question_id))

