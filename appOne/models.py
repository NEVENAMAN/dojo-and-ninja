from django.db import models

class Dojo(models.Model):
    name = models.CharField(max_length=60)
    city= models.CharField(max_length=60)
    state = models.CharField(max_length=60)

class Ninjas(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    dojo_id = models.ForeignKey(Dojo,related_name="ninjas",on_delete=models.CASCADE)
    

def creatDojo(request):
    name = request.POST['name']
    city = request.POST['city']
    state = request.POST['state']
    Dojo.objects.create(name=name , city = city , state = state)
    

def creatNinja(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    dojo = Dojo.objects.get(id = request.POST['dojo'])

    Ninjas.objects.create(first_name = first_name , last_name = last_name , dojo_id = dojo)

def get_all_dojo(request):
    return Dojo.objects.all()

def get_all_ninja(request):
    return Ninjas.objects.all()

def delete_dojo(id):
    dojoID = Dojo.objects.get( id = id)
    print("****************")
    return dojoID.delete()