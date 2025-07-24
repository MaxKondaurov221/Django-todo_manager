from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView


# Create your views here.
def index_view(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        template_name='todo_about/index.html',
    )

