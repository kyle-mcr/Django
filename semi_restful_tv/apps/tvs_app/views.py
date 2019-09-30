from django.shortcuts import render, HttpResponse, redirect
from .models import Show
from django.contrib import messages

def index(request):
    context = {
        'shows' : Show.objects.all(),
    }
    return render(request, "tvs_app/index.html", context)

def show(request, get_id):
    context = {
        'show' : Show.objects.get(id=get_id),
    }
    return render(request, "tvs_app/show.html", context)

def new(request):
    if request.method=='POST':
         errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/show/new')
    else:                
        new_show = Show.objects.create(title=request.POST['title'], network=request.POST['network'], 
        release=request.POST['release'], description=request.POST['desc'])
        new = new_show.id
    return redirect('/show/{}'.format(new))

def addpage(request):
    return render(request, "tvs_app/new.html")

def edit(request, get_id):
    context = {
        'show' : Show.objects.get(id=get_id),
    }
    return render(request, "tvs_app/edit.html", context)

def delete(request, get_id):
    delete = Show.objects.get(id=get_id)
    delete.delete()
    return redirect('/')

def update(request,get_id):
    edit_show = Show.objects.get(id=get_id)
    edit_show.title= request.POST['title']
    edit_show.network= request.POST['network']
    edit_show.release= request.POST['release']
    edit_show.description= request.POST['desc']
    edit_show.save()
    return redirect('/show/'+get_id)

 