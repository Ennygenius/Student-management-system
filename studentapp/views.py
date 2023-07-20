from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from .models import Student
from django.core.paginator import Paginator
from .forms import addStudent
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def index(request):
    students = Student.objects.all()
    paginator = Paginator(students,3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'index.html', { 'students': page_obj})


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

def logout_view(request):
    logout(request)
    return redirect('/')