from django.shortcuts import render ,redirect
from .models import Category, Photo
from django.views.generic.list import ListView




class PhotoList(ListView):
    model= Photo
    context_object_name='gallery'
    template_name='/photos/gallery'

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)

        return context

    
# Create your views here.

def gallery(request):
    category= request.GET.get('category')
    if category == None:
        photos= Photo.objects.all()
    else:
        photos= Photo.objects.filter(category__name=category)
 
    categories= Category.objects.all()
    
    context={'categories':categories ,'photos':photos}
    return render(request,'photos/gallery.html',context)

def viewPhoto(request, pk):
    photo= Photo.objects.get(id=pk)
    return render(request,'photos/photo.html',{'photo':photo})

def addPhoto(request):
    category= Category.objects.all()
    if request.method == 'POST' :
        data = request.POST
        image= request.FILES.get('image')

        if data['category'] != 'none' :
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category , created= Category.objects.get_or_create(name=data['category_new'])
        else:
            category= None
        
        photo = Photo.objects.create(
            category=category,
            description = data['description'],
            image=image,
        )
        return redirect('gallery')

    context={'categories':category }

    return render(request,'photos/add.html',context)