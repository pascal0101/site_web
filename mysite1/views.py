from django.shortcuts import render
from .models import Post 
from .models import Galerie
from .models import Image
# Create your views here.
def index(request):
    #posts = Post.objects.all()
    return render(request,'index.html')

def test(request):
    posts = Post.objects.all()
    return render(request,'index.html',{'posts':posts})

def about(request):
    #post = Post.objects.get(id=id)
    return render(request,'about.html')

def getgalerie(request):
    #images = Image.objects.all()
    galeries = Galerie.objects.all()
    return render(request,'index.html',{'galeries':galeries})

def getimage(request):
    images = Image.objects.all()
    return render(request,'index.html',{'images':images})

def getgaleri1(request):
    images = Images.objects.all()
    for gal in images:
       img = Image.objects.filter(categorie=gal)
       print(img)
    return render(request,'index.html',{'galeries':galeries})