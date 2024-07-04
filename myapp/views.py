from django.shortcuts import render, redirect, get_object_or_404 # type: ignore
from django.http import HttpResponse # type: ignore
from .models import User, Illustration, Collections, Tools
from django.db.models import Q # type: ignore
from django.contrib.auth import authenticate, login # type: ignore
from django.contrib.auth.decorators import login_required # type: ignore
from .forms import CollectionForm, IllustrationForm, ToolsForm
# Create your views here.

def home(request):
    favorite_collections = Collections.objects.filter(is_favorite=True)[:3]
    query = request.GET.get('query', "")
    illustrations = Illustration.objects.filter(collection__in=favorite_collections)
    return render(request, 'myapp/home.html', {'favorite_collections': favorite_collections, 'illustrations': illustrations})



def illustration_list(request):
    illustrations = Illustration.objects.all()
    return render(request, 'myapp/illustrations_list.html', {'illustrations': illustrations})

def collection_list(request):
    collections = Collections.objects.all()
    return render(request, 'myapp/collections_list.html', {'collections': collections})

def collection_details(request, id):
    collection = get_object_or_404(Collections, id=id)
    return render(request, 'myapp/collection_detail.html', {'collection': collection})





def about(request):
    return render(request, 'myapp/about.html')

def contact(request):
    return render(request, "myapp/contact.html")


@login_required(login_url='/login/')
def profile(request, id):
    user = User.objects.get(id=int(id))
    
    # birds = user.birds.all()

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
            pass

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:

            pass

    context = {'page': page}
    return render(request, 'myapp/login_register.html', context)


def add_collection(request):
    form = CollectionForm()
    illustration_form = IllustrationForm()
    collections = Collections.objects.all()
    tools = Tools.objects.all()
    tool_form= ToolsForm()
   
    if request.method == 'POST':
        collection_title = request.POST.get('title')
        collection_description = request.POST.get('description')
        collection_is_favorite = request.POST.get('is_favorite')
        illustration_tools = request.POST.get('tool')
        collection = request.POST.get('collection')


        title, created = Collections.objects.get_or_create(title=collection_title)
        description, created = Collections.objects.get_or_create(description=collection_description)
        is_favorite, created = Collections.objects.get_or_create(is_favorite=collection_is_favorite)
        tool, created = Collections.objects.get_or_create(name=illustration_tools )

        form = CollectionForm(request.POST)
        illustration_form = IllustrationForm(request.POST)
        tool_form= ToolsForm(request.POST)

        new_collection = Collections(title=title, description=description, is_favorite=is_favorite )
        new_collection.save()

        new_illustration = Illustration(image=request.FILES['image'])
        
        new_illustration.save()
        new_illustration.add(tool)
        return redirect('home')
        
    context = {'form': form, 'illustration_form': illustration_form, 'tools': tools, 'collections': collections}
    return render(request, 'myapp/add_collection.html', context)

