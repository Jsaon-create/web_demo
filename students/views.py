from django.http import HttpResponse
from django.shortcuts import render
from students import models


# Create your views here.
def index(request):
    method = request.method
    if method == 'GET':
        return render(request, 'index.html')
    else:
        name = request.POST.get('username', '')
        password = request.POST.get('password', '')
        if name and password:
            student = models.Students(name=name, password=password)
            student.save()
            return HttpResponse('注册成功！')
        return HttpResponse('字符为空！')


def show(request):
    student_list = models.Students.objects.all()
    return render(request, 'show.html', {'student': student_list})
