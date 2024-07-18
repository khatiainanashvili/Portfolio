from functools import wraps
from django.shortcuts import render, redirect, get_object_or_404 # type: ignore
from django.http import HttpResponse, HttpResponseForbidden # type: ignore
from .models import User, Illustration, Collections, Tools, Comment
from django.db.models import Q # type: ignore
from django.contrib.auth import authenticate, login, logout # type: ignore
from django.contrib.auth.decorators import login_required # type: ignore
from .forms import CollectionForm, CollectionUpdateForm, IllustrationForm, ToolsForm, UserCreationForm, UserForm
from .seeder import seeder_func
from django.contrib import messages
# Create your views here.

def home(request):
    favorite_collections = Collections.objects.filter(is_favorite=True)[:3]
    
    seeder_func()
    illustrations = Illustration.objects.filter(collection__in=favorite_collections)
    return render(request, 'myapp/home.html', {'favorite_collections': favorite_collections, 'illustrations': illustrations})


# SUPERUSER REQUIRED 
def superuser_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            from django.contrib.auth.views import redirect_to_login
            return redirect_to_login(request.get_full_path())
        if not request.user.is_superuser:
            return HttpResponseForbidden("You are not allowed to perform this action.")
        return view_func(request, *args, **kwargs)
    return _wrapped_view

def illustrations_list(request):
    query = request.GET.get('query') if request.GET.get('query') != None else ""
    tools = Tools.objects.all()
    illustrations = Illustration.objects.filter(tool__name__icontains=query)
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


    collection_comment = collection.comment_set.all()
    
    if request.method == 'POST':
         if not request.user.is_authenticated:
            messages.info(request, 'You need to log in to post a comment.')
            return redirect('login')
         
         else:
            comment = Comment.objects.create(
            user=request.user,
            collection=collection,  
            body=request.POST.get('body')
        )
            return redirect('collection_detail', id=id) 

    return render(request, 'myapp/collection_detail.html', {'collection': collection, "illustration": illustration, 'comments': collection_comment})




@superuser_required
def delete_collection(request, id):
    collection = Collections.objects.get(id=id)
    user = request.user
    if request.method == 'POST':
        collection.delete()
        return redirect('collections')
    return render(request, "myapp/delete_collection.html", {'collection': collection, "user": user})


@superuser_required
def delete_illustration(request, id):
    illustration = Illustration.objects.get(id=id)
    user = request.user
    if request.method == 'POST':
        illustration.image.delete()
        illustration.delete()
        return redirect('illustrations')
    return render(request, "myapp/delete_illustration.html", {'illustration': illustration, "user": user})


def delete_comment(request, id):
   
    user = request.user
    comment = Comment.objects.get(id=id)
    if request.method == 'POST':
        comment.delete()
        return redirect('collections')
    return render(request, "myapp/delete_comment.html", {'comment': comment, "user": user})



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



def log_out(request):
    logout(request)
    return redirect('home')


def register_page(request):

    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')

    context = {'form': form}
    return render(request, 'myapp/login_register.html', context)


@superuser_required
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


@login_required
def update_user(request):
    user = request.user 
    form = UserForm(instance=user)
    if request.method == "POST":
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile', user.id)  
    return render(request, 'myapp/update_user.html', {'form': form})


@superuser_required
def update_collection(request, collection_id):
    collection = get_object_or_404(Collections, id=collection_id)
    collection_form = CollectionUpdateForm(instance=collection)
    illustrations = Illustration.objects.filter(collection=collection)
    illustration_forms = [IllustrationForm(instance=illustration) for illustration in illustrations]

    if request.method == "POST":
        collection_form = CollectionUpdateForm(request.POST, instance=collection)
        
        if collection_form.is_valid():
            updated_collection = collection_form.save(commit=False)
            updated_collection.save()
            for form in illustration_forms:
                if form.is_valid():
                    form.save()
            new_illustration_form = IllustrationForm(request.POST, request.FILES)
            if new_illustration_form.is_valid():
                new_illustration = new_illustration_form.save(commit=False)
                new_illustration.collection = collection
                new_illustration.save()

            return redirect('collection_detail', collection.id)
    
    else:
        new_illustration_form = IllustrationForm()

    return render(request, 'myapp/update_collection.html', {
        'collection_form': collection_form,
        'illustration_forms': illustration_forms,
        'new_illustration_form': new_illustration_form,
        'collection': collection
    })