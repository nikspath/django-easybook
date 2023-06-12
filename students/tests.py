from django.test import TestCase
from .models import *
from departments.models import Department
# Create your tests here.
from faker import Faker
fake = Faker()
import random

def seed_db(n=10):
	try:
		for i in range(0,n):
			depart_obj=Department.objects.all()
			department_indx=random.randint(0,len(depart_obj)-1)
			department=depart_obj[department_indx]
			stdid=f"std{random.randint(2,100)}"
			stdid_obj=StudentID.objects.create(studentid=stdid)
			Student.objects.create(
				department=department,
				studentid=stdid_obj,
				std_name=fake.name(),
				std_email=fake.email(),
				std_age=random.randint(20,30),
				std_address=fake.address()
				)
	except Exception as e:
		return e		


def create_marks():
	try:
		student_obj=Student.objects.all()
		sub_obj = Subject.objects.all()
		for s in student_obj:
			for sub in sub_obj:
				StudentMarks.objects.create(
						student=s,
						subject=sub,
						marks=random.randint(0,100)
					)
	except Exception as e:
		print(e)		
		


