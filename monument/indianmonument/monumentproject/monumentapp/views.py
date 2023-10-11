from django.shortcuts import render, redirect
from .models import Monument
from .forms import MonuForm
# Create your views here.



def index(request):
    monument=Monument.objects.all()
    return render(request,'index.html',{'monument':monument})
def detail(request,id):
    monument=Monument.objects.get(id=id)
    return render(request,'detail.html',{'Result':monument})
def add(request):
    if request.method=='POST':
        name=request.POST.get('name')
        about=request.POST.get('about')
        year=request.POST.get('year')
        image=request.FILES['image']
        monument=Monument(name=name,about=about,year=year,image=image)
        monument.save()
    return render(request,'add.html')
def update(request,id):
    monument=Monument.objects.get(id=id)
    form=MonuForm(request.POST or None,request.FILES,instance=monument)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'object':form,'monu':monument})
def delete(request,id):
    if request.method =='POST':
        monument=Monument.objects.get(id=id)
        monument.delete()
        return redirect('/')
    return render(request,'delete.html')


