from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
from django.db.models import Q,Sum

# Create your views here.

def student_detail(request, std_id):
	data= StudentMarks.objects.filter(student__studentid__studentid=std_id)
	total_marks=data.aggregate(Sum('marks'))
	std=Student.objects.annotate(marks=Sum('studentmarks__marks')).order_by('-marks')
	rank=1
	for i in std:
		rank += 1
		if i.marks == total_marks['marks__sum']:
			break
	return render(request,'student_detail.html',context={'student_data':data,'total_marks':total_marks,'rank':rank})



def student_report(request):
	if request.GET.get('search'):
		data=Student.objects.filter(
			Q(std_name__icontains = request.GET.get('search'))|
			Q(department__department__icontains = request.GET.get('search'))
				)
	else:	
		data=Student.objects.all()
	paginator = Paginator(data, 5)
	page_number = request.GET.get("page")
	page_obj = paginator.get_page(page_number)
	return render(request,'students.html',context={'student_data':page_obj})