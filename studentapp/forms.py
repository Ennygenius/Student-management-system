from django import forms
from .models import Student

class addStudent(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"


class editStudent(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"