from django.shortcuts import render, redirect
from django.urls import reverse
from .models import*

# Create your views here.
def masterlogin(request):
    return render(request, 'master/index.html')

def addcategory(request):
    if request.method == "POST":
        category_name = request.POST.get('name')
        Category.objects.create(name=category_name)
        return redirect("category")

    else:
        return render(request, "master/addcategory.html")

def category(request):
    category_obj=Category.objects.all()
    context={'category_obj':category_obj}
    return render(request, "master/category.html",context)
    
def deletecategory(request,id):
    obj=Category.objects.get(id=id)
    obj.delete()
    return redirect("category")

def editcategory(request,id):
    if request.method =="GET":
        obj=BaseContent.objects.get(id=id)
        obj=Category.objects.get(id=id)
        context={'obj':obj,'obj':obj}
        return render(request,'master/editcategory.html',context)
    elif request.method =="POST":
        is_active=request.POST['is_active']
        obj=BaseContent.objects.get(id=id)
        category_name=request.POST['name']
        obj=Category.objects.get(id=id)
        obj.is_active=is_active
        obj.name=category_name
        obj.save()
        return redirect("category")
    
def addsubcategory(request,id):
    subcategoryobj= Category.objects.get(id = id)

    if request.method == "POST":
        sub_name = request.POST['subname']
        SubCategory.objects.create(subname = sub_name, Category_id=subcategoryobj)
        return redirect(reverse('addsubcategory', args=[id]))
    else:    
        subobj=SubCategory.objects.filter(Category_id_id=subcategoryobj)
        context={'obj':subcategoryobj, 'subobj':subobj}
        return render(request,'master/addsubcategory.html', context)

def deletesub(request,id):
    delete_obj=SubCategory.objects.get(id=id)
    category_id = delete_obj.Category_id_id
    delete_obj.delete()
    return redirect(reverse('addsubcategory', args=[category_id]))

def editsub(request,id):
    if request.method =="GET":
        obj=SubCategory.objects.get(id=id)
        context={'obj':obj}
        return render(request,'master/editsub.html', context)
    elif request.method =="POST":
        
        sub_name=request.POST['subname']
        obj=SubCategory.objects.get(id=id)
        obj.subname=sub_name
        obj.save()
        category_id = obj.Category_id_id
        return redirect(reverse('addsubcategory', args=[category_id]))

