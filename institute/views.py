from django.shortcuts import render

from institute.models import *

def center_calendar(request, id):
	lectures = Lecture.objects.filter(batch__center__id = id)

	events = []
	for lecture in lectures:
		event = {
		'start': lecture.date.strftime("%Y-%m-%d"),
		'title': lecture.code
		}
		events.append(event)


	return render(request, 'institute/calendar.html', {'events': events})
