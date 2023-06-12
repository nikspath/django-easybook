from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Books
from .serializers import BookSerializer
# Create your views here.

@api_view(['GET'])
def books(request):
	return Response({'success':'first api'})

@api_view(['GET'])
def all_books(request):
	books=Books.objects.all()
	serializerdata=BookSerializer(books,many=True)
	return Response({"success":serializerdata.data})	

@api_view(['POST'])
def create_books(request):
	if request.data:
			serializer=BookSerializer(data=request.data)
			if serializer.is_valid():
				serializer.save()
				return Response({"success":"saved success"})
			else:
				return Response({"Error":serializer.error})
	else:
		return Response({"error":"data not valid"})			


@api_view(['DELETE'])
def delete_books(request):
	book_id=request.data.get('book_id')
	try:
		book=Books.objects.get(id=book_id)		
		book.delete()
		return Response({"success":"deleted successflly"})
	except Exception as e:
		return Response(e)	

@api_view(['PUT'])
def update_book(request):
	try:
		book=Books.objects.get(id=request.data.get('book_id'))
		book.name=request.data.get('name')
		book.ratting=request.data.get('ratting')
		book.is_published=request.data.get('is_published')	
		book.save()
		return Response({"Sucess":"updated successfully"})
	except Exception as e:
		return Response(e)	

