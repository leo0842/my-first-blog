from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Person
def aindex(request):
    return HttpResponse("어서오세요. 홈페이지입니다.")

def index2(request):
    asdf = Person.a
    aa = Person.b
    context = {"asdf":asdf}
    return render(request, 'mysite/index.html', context)
# Create your views here.
