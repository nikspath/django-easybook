from django.db import models
from departments.models import Department
# Create your models here.


class StudentID(models.Model):
	studentid = models.CharField(max_length=100)

	def __str__(self):
		return self.studentid

class StudentManger(models.Manager):
	def get_queryset(self):
		return super().get_queryset().filter(is_deleted=False)		


class Student(models.Model):
	department=models.ForeignKey(Department,on_delete=models.CASCADE)
	studentid=models.OneToOneField(StudentID, on_delete=models.CASCADE)
	std_name=models.CharField(max_length=100)
	std_email=models.CharField(max_length=100,unique=True)
	std_age=models.IntegerField()
	std_address=models.CharField(max_length=100)
	is_deleted=models.BooleanField(default=False)

	objects=StudentManger()
	admin_objects=models.Manager()

	def __str__(self):
		return self.std_name

	class Meta:
		ordering=['std_name']


class Subject(models.Model):
	subject_name=models.CharField(max_length=100)

	def __str__(self):
		return self.subject_name

class StudentMarks(models.Model):
	student = models.ForeignKey(Student, related_name="studentmarks", on_delete=models.CASCADE)
	subject = models.ForeignKey(Subject, related_name="subject", on_delete=models.CASCADE)
	marks = models.IntegerField()

	def __str__(self):
		return f'{self.student.std_name} - {self.subject.subject_name}  '

	class Meta:
		unique_together=['student','subject']	
		ordering =['student__std_name']


