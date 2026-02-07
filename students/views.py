from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.
#web application endpoint
def students(request):
    students = [
        {
            'id' : 1,
            'name' : 'Abdullah',
            'age' : 24
        }
    ]
    return HttpResponse(students)