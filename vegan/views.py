from django.shortcuts import render,redirect
from .models import Receipe
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url="/login/")
def receipe(request):
	receipe_all=Receipe.objects.all()
	return render(request,"receipe.html", context={"page":"receipe","receipe_all":receipe_all})


def receipe_form(request):
	if request.method == 'POST':
		data=request.POST
		receipe_img=request.FILES.get('receipe_img')
		receipe_name=data.get('receipe_name')
		receipe_description=data.get('receipe_description')
		if data.get('type') == 'add':
			Receipe.objects.create(name=receipe_name,description=receipe_description,image=receipe_img)
		else:
			recepe=Receipe.objects.get(id=data.get('id'))
			recepe.name=receipe_name
			recepe.description=receipe_description
			if receipe_img:
			 	recepe.image=receipe_img 
			recepe.save()

	return redirect("/receipe")		
				

def delete_receipe(request,id):
	Receipe.objects.get(id=id).delete()
	return redirect("/receipe")	


def update_receipe(request,id):
	data=Receipe.objects.filter(id=id).first()
	receipe_all=Receipe.objects.all()
	return render(request,"receipe.html", context={"page":"receipe","receipe_all":receipe_all,"edit_receipe":data})

