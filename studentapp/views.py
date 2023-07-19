from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from .models import Student
from django.core.paginator import Paginator
from .forms import addStudent
from django.contrib.auth import authenticate,login

# Create your views here.
def index(request):
    students = Student.objects.all()
    
    return render(request, 'index.html', { 'students': students})


@login_required(login_url="/accounts/login/")
def add(request):
    if request.method == 'POST':
        form = addStudent(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = addStudent()
    return render(request, 'addStudent.html', {'form': form })



@login_required(login_url="/accounts/login/")
def edit(request, id):
     
    students = Student.objects.get(pk=id)

    if request.method == 'POST':
        form = addStudent(request.POST, request.FILES, instance=students)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = addStudent( instance=students)
        return render(request, 'edit.html', {'form': form})


@login_required(login_url="/accounts/login/")
def deleteStudent(request, id):
    student = Student.objects.get(pk=id)
    student.delete()
    return redirect('/confirm')


def confirmDelete(request):
    return render(request, 'confirmDelete.html')


def details(request, id):
    student = Student.objects.get(pk=id)
    return render(request, 'details.html', {'student' : student})

# def signin(request):
#     if request.method == "POST":
#         username = request.get.POST('username')
#         password = request.get.POST('password')
        
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('index')
#             ...
#         else:
#             return redirect('signin')
#     else:
#         return render(request,
#                    'signin.html')