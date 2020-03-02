from django.shortcuts import get_object_or_404, render
from .models import *
from django.contrib import messages
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
    images = Image.objects.all()
    return render(request,'index.html',{'galeries':galeries,'images':images})

def getdetail(request,id):
    galerie = get_object_or_404(Galerie, pk=id)
    comments = Comment.objects.filter(gal_id=id)
    cmt = Comment.objects.filter(gal_id=id).count()
    print(cmt)
    if request.method == 'POST':
        nom_c = request.POST.get('nom')
        email_c = request.POST.get('email')
        message_c = request.POST.get('message')
        gal_id = Galerie.objects.get(pk=id)
        print("form is ok")
        c = Comment(nom=nom_c,email= email_c,message= message_c,gal= gal_id)
        c.save()
        messages.success(request,'Commentaire a été posté avec succès')
        return render(request,'detail.html', {'galerie': galerie,'comments':comments,'cmt':cmt})
       
    else:
        return render(request,'detail.html', {'galerie': galerie,'comments':comments,'cmt':cmt})
    
    
    
    
def getimage(request):
    images = Image.objects.all()
    return render(request,'index.html',{'images':images})

def getgaleri1(request):
    images = Images.objects.all()
    for gal in images:
       img = Image.objects.filter(categorie=gal)
       print(img)
    return render(request,'index.html',{'galeries':galeries})