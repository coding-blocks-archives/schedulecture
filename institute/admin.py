from django.contrib import admin
from .models import *

class LectureHallAdmin(admin.ModelAdmin):
	list_display = ('code', 'center', 'capacity')

class BatchAdmin(admin.ModelAdmin):
	list_display = ('code', 'course', 'center', 'capacity')

class LectureAdmin(admin.ModelAdmin):
	list_display = ('code', 'batch', 'hall', 'teacher', 'date', 'start_time', 'end_time')

	def teacher(self, lecture):
		return lecture.batch.teacher

admin.site.register(Center)
admin.site.register(LectureHall, LectureHallAdmin)
admin.site.register(Course)
admin.site.register(Teacher)
admin.site.register(Batch, BatchAdmin)
admin.site.register(Lecture, LectureAdmin)
