from django.contrib.messages import success
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import ToDoCreateItemForm, ToDoItemUpdateForm
from .models import ToDoItem

# Create your views here.


def index_view(request: HttpRequest) -> HttpResponse:
    todo_items = ToDoItem.objects.all()
    return render(
        request,
        template_name='todo_list/index.html',
        context={'todo_items': todo_items[:3]},
    )

class ToDoListIndexView(ListView):
    template_name = 'todo_list/index.html'
    queryset = ToDoItem.objects.all()[:3]

class ToDoListView(ListView):
    queryset = ToDoItem.objects.filter(archived=False)


class ToDoListDoneView(ListView):
    queryset = ToDoItem.objects.filter(done=True).all()

class ToDoDetailView(DetailView):
    queryset = ToDoItem.objects.filter(archived=False)

class ToDoItemCreateView(CreateView):
    model = ToDoItem
    form_class = ToDoCreateItemForm

class ToDoItemUpdateView(UpdateView):
    model = ToDoItem
    form_class = ToDoItemUpdateForm
    template_name_suffix = '_update_form'

class ToDoItemDeleteView(DeleteView):
    model = ToDoItem
    success_url = reverse_lazy('todo_list:list')

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.archived = True
        self.object.save()
        return HttpResponseRedirect(success_url)