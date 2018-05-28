from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Question
def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	#output = ', '.join([q.question_text for q in latest_question_list])

	#template = loader.get_template('polls/index.html')
	context = {
		'latest_question_list': latest_question_list,
	}
	return render(request, 'polls/index.html', context)
	#return HttpResponse(output)
# Create your views here.
def detail(request, question_id):
	"""
	try:
		question = Question.objects.get(pk=question_id)
	except:
		raise Http404("Question does not exist")
	"""
	question = get_object_or_404(Question, pk=question_id)

	return render(request,'polls/detail.html', {'question':question})

def results(request, question_id):
	#question = get_object_or_404(Question, pk=question_id)
	#return render(request, 'polls/results.html',{'question':question})
	response = "You're looking at the results of question {}"
	return HttpResponse(response.format(question_id))

def vote(request, question_id):
	#question = get_object_or_404(Question, pk=question_id)
	#try:
	#	selected_choice = question.choice_set.get(pk=request.POST['choice'])
	#except (KeyError, Choice.DoesNotExist):
	#	return render(request, 'polls/detail.html',{'question': question, 'error_message':"You didn't select a choice."})
	#else:
	#	selected_choice.votes += 1
	#	selected_choice.save()
	#return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
	return HttpResponse("You're voting on question {}".format(question_id))


