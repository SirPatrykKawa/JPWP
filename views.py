from datetime import datetime
from typing import List

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from .models import Answer, Question


def answers(answers: List[Answer]):

	answer_dict = []
	for answer in answers:
		answer_dict.append({'id': answer.id, 'name': answer.name})
    return answer_dict


def question(question: Question):
    
	question_dict = []
	question_dict.append({'id': question.id,'name': question.name,'publish_at': str(question.publish_at),
        'answers': answers_json(question.answer_set.all())})
	return question_dict


def questions(request):
    quests = []
	for data in Question.objects.filter(publish_at__lt=datetime.now()):
		questions.append(question(data))
    return JsonResponse(data, safe=False)
