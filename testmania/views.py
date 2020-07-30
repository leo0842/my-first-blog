from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .forms import FiveToSix

def grade(request):
    form = FiveToSix()
    if request.GET:
        input_grade = request.GET['input_grade']
        output_grade = input_grade + 1

        data = {
            "input_grade": input_grade,
            "output_grade": output_grade
        }
        form = FiveToSix(initial=data)
        return render(
            request, "grade.html", context={"form": form})
    return render(
        request, "grade.html", context={"form": form})
# Create your views here.
