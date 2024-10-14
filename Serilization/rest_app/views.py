from django.shortcuts import render
from .models import Student
from .seriealizers import Studentseriealizers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
# Create your views here.


# Model object 


def student_Details(request,pk):
    # stu = Student.objects.get(id =3)
    stu = Student.objects.get(id = pk)
    seriealizers = Studentseriealizers(stu)
    json_data = JSONRenderer().render(seriealizers.data) 
    return HttpResponse(json_data, content_type = "application/json")
    
    
    
def student_list(request):
    stu = Student.objects.all()
    seriealizers = Studentseriealizers(stu,many= True)
    # json_data = JSONRenderer().render(seriealizers.data)
    # return HttpResponse(json_data, content_type = "application/json")
    
    return JsonResponse(seriealizers.data, safe=False)
      
    