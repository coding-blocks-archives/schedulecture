from django.db import models
from django.contrib.auth.models import User


class Center(models.Model):
	name = models.CharField(max_length = 30)
	address = models.TextField(max_length = 255, default = None)

	def __str__(self):
		return self.name


class LectureHall(models.Model):
	code = models.CharField(max_length = 10)
	center = models.ForeignKey(Center)
	capacity = models.IntegerField(default = 0)

	def __str__(self):
		return self.code


class Course(models.Model):
	name = models.CharField(max_length = 30)

	def __str__(self):
		return self.name


class Teacher(models.Model):
	name = models.CharField(max_length = 20)

	def __str__(self):
		return self.name


class Batch(models.Model):
	code = models.CharField(max_length = 20)
	course = models.ForeignKey(Course)
	center = models.ForeignKey(Center)
	teacher = models.ForeignKey(Teacher)
	capacity = models.IntegerField(default = 0)
	start_date = models.DateField(null = True, blank = True)
	end_date = models.DateField(null = True, blank = True)


	def __str__(self):
		return self.code 

	class Meta:
		verbose_name_plural = "Batches"


class Lecture(models.Model):
	code = models.CharField(max_length = 20)
	batch = models.ForeignKey(Batch)
	hall = models.ForeignKey(LectureHall)
	date = models.DateField(null = True, blank = True)
	start_time = models.DateTimeField(null= True, blank = True)
	end_time = models.DateTimeField(null = True, blank = True)

	def __str__(self):
		return self.batch.code