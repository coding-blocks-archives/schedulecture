from django.shortcuts import render
from django.utils.dateparse import parse_datetime
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect

from institute.models import *
import json

def center_calendar(request, id):
	lectures = Lecture.objects.filter(batch__center__id = id)

	events = []
	for lecture in lectures:
		event = {
		'l_id': lecture.id,
		'start': lecture.date.strftime("%Y-%m-%d"),
		'title': lecture.code
		}
		events.append(event)


	return render(request, 'institute/calendar.html', 
		{'events': events, 'center_id': id})


@csrf_protect
def save_center_calendar(request, id):
	events = json.loads(request.POST['data'])
	for event in events:
		lecture = Lecture.objects.get(id = event['l_id'])
		lecture.date = parse_datetime(event['date'])
		lecture.save()
	return JsonResponse({'success': True})
	