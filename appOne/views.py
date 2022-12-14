from django.shortcuts import render,redirect

from appOne import models

def index(request):
    dataDojo = models.get_all_dojo(request)
    dataNinja = models.get_all_ninja(request)
    context = {
        'dataDojo' : dataDojo,
        'dataNinja' : dataNinja
    }
    print(dataDojo)
    return render(request,'index.html',context)

def registerDojo(request):
    if request.method == "POST":
       id = models.creatDojo(request)
       request.session['id'] = id
    return redirect('/get_all')

def redisterNinja(request):
    if request.method == "POST":
        models.creatNinja(request)
    return redirect('/get_all')

def get_dojo(request):
    print("*****************")
    dataDojo = models.get_all_dojo(request)
    dataNinja = models.get_all_ninja(request)
    context = {
        'dataDojo' : dataDojo,
        'dataNinja' : dataNinja
    }
    return render(request,'index.html',context)

def delete(request,id):
        print("***************")
        print(id)
        models.delete_dojo(id)
        return redirect("/")

