from django.shortcuts import render, redirect
from .models import Position
from .forms import PosForm
from django.views.generic import DeleteView, UpdateView
from .filters import PostFilter


def index(request):
    positions_all = Position.objects.all()
    positions = PostFilter(request.GET, queryset=positions_all)
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'positions': positions})


def about(request):
    return render(request, 'main/about.html')


def service(request):
    return render(request, 'main/service.html')


def add(request):
    error = ''
    if request.method == 'POST':
        form = PosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма заполнена неправильно или не до конца'
    form = PosForm()
    context = {
        'form': form
    }
    return render(request, 'main/add.html', context)


class Delete(DeleteView):
    model = Position
    success_url = '/'
    template_name = 'main/delete.html'


class Update(UpdateView):
    model = Position
    template_name = 'main/add.html'
    form_class = PosForm
    success_url = '/'
