from django.shortcuts import render, redirect, get_object_or_404 # type: ignore
from django.http import HttpResponse # type: ignore
from .models import User, Illustration, Collections, Tools
from django.db.models import Q # type: ignore
from django.contrib.auth import authenticate, login # type: ignore
from django.contrib.auth.decorators import login_required # type: ignore
from .forms import CollectionForm, IllustrationForm, ToolsForm
from .seeder import seeder_func
from django.contrib import messages
# Create your views here.

def home(request):
    favorite_collections = Collections.objects.filter(is_favorite=True)[:3]
    
    seeder_func()
    illustrations = Illustration.objects.filter(collection__in=favorite_collections)
    return render(request, 'myapp/home.html', {'favorite_collections': favorite_collections, 'illustrations': illustrations})



def illustrations_list(request):
    query = request.GET.get('query', "")
    tools = Tools.objects.all()
    illustrations = Illustration.objects.filter(Q(tool__name__icontains=query))
    return render(request, 'myapp/illustrations_list.html', {'illustrations': illustrations, "tools": tools})

def illustration_detail(request, id):
    illustration = get_object_or_404(Illustration, id=id)
  
    return render(request, 'myapp/illustration_detail.html', {'illustration': illustration})

def collections_list(request):
    collections = Collections.objects.all()
    return render(request, 'myapp/collections_list.html', {'collections': collections})

def collection_details(request, id):
    collection = get_object_or_404(Collections, id=id)
    illustration = get_object_or_404(Illustration, id=id)
    return render(request, 'myapp/collection_detail.html', {'collection': collection, "illustration": illustration})


def delete_collection(request, id):
    collection = Collections.objects.get(id=id)
    user = request.user
    if request.method == 'POST':
        collection.delete()
        return redirect('collections')
    return render(request, "myapp/delete_collection.html", {'collection': collection, "user": user})

def delete_illustration(request, id):
    illustration = Illustration.objects.get(id=id)
    user = request.user
    if request.method == 'POST':
        illustration.delete()
        return redirect('illustrations')
    return render(request, "myapp/delete_illustration.html", {'illustration': illustration, "user": user})


def contact(request):
    return render(request, "myapp/contact.html")


@login_required(login_url='/login/')
def profile(request, id):
    user = User.objects.get(id=int(id))
    headline= "My Favorite Birds"
    context = {"user": user, "headline": headline}
    return render(request, "myapp/profile.html", context)



def login_page(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home') 

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, "Username doesn't exit")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "User or Password is Incorrect")
            

    context = {'page': page}
    return render(request, 'myapp/login_register.html', context)

@login_required(login_url='/login/')
def add_collection(request):
    form = CollectionForm()
    illustration_form = IllustrationForm()
    collections = Collections.objects.all()
    tools = Tools.objects.all()

    if request.method == 'POST':
        collection_name = request.POST.get('collection_name')
        collection_description = request.POST.get('description')
        collection_is_favorite = True if request.POST.get('is_favorite') == "on" else False
        illustration_tool_name = request.POST.get('tools')
        
        collection, created = Collections.objects.get_or_create(name=collection_name, description = collection_description, is_favorite = collection_is_favorite)

        tool, created = Tools.objects.get_or_create(name=illustration_tool_name)

        new_illustration = Illustration(
            image=request.FILES.get('image'),
            name=illustration_form.data.get('name', ''),
            tool=tool,
            description=illustration_form.data.get('description', ''),
            collection=collection
        )

        new_illustration.save()

        return redirect('home')

    context = {'form': form, 'illustration_form': illustration_form, 'tools': tools, 'collections': collections}
    return render(request, 'myapp/add_collection.html', context)
