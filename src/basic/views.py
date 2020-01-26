from django.shortcuts import render
from .flames import flames

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request , 'home.html', {})

def print_names(request, *args, **kwargs):

    name1 = request.GET.get('name1')
    name2 = request.GET.get('name2')
    prediction = flames(name1, name2)

    context = {
        'n1' : name1.capitalize(),
        'n2' : name2.capitalize(),
        'p'  : prediction,
    }
    return render(request, '3d_name.html', context )

def name_bg(request, *args, **kwargs):

    name1 = request.GET.get('name1')
    name2 = request.GET.get('name2')
    prediction = flames(name1, name2)

    context = {
        'n1' : name1.capitalize(),
        'n2' : name2.capitalize(),
        'p'  : prediction,
    }

    return render(request, '3d_name.html', context)

