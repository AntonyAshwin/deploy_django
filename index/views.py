from urllib import request
from django.shortcuts import render, HttpResponse, redirect
from .forms import FinalForm


# Create your views here.

def home(req):
    if req.method == 'POST':
        form = FinalForm(req.POST)
        if form.is_valid():
            form.save()
            context = {'error': 'Your form has been saved', 'data': form}
            return render(req, 'index.html', context)
        else:
            context = {'error': 'Your form hasnt been saved', 'data': form}
            return render(req, 'index.html', context)
    else:
        context = {}
        form = FinalForm()
        context['data'] = form
        return render(req, 'index.html', context)
