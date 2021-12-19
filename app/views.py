from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt

# ---------- Index ----------

def index(request):
    return render(request, "index.html")

# ---------- About ----------

def about(request):
    currentEvents = Event.objects.filter(eventStatus=0)
    pastEvents = Event.objects.filter(eventStatus=1)
    context = {
        'currentEvents': currentEvents,
        'pastEvents': pastEvents,
    }
    return render(request, 'about.html', context)

# ---------- Books ----------
def books(request):
    books = Product.objects.filter(prodType=0)
    context = {
        'books': books,
    }
    print(theBooks)
    return render(request, 'books.html', context)

# ---------- Art ----------
def art(request):
    arts = Product.objects.filter(prodType=1)
    context = {
        'arts': arts,
    }
    return render(request, 'art.html', context)


# ---------- Services ----------
def services(request):
    return render(request, 'services.html')

# ---------- Contact ----------
def contact(request):
    return render(request, 'contact.html')

# ---------- Admin ----------
def theAdmin(request):
    if 'user_id' not in request.session:
        messages.error(request, 'Please Log in to view')
        return redirect('/login/')
    else:
        user = User.objects.get(id=request.session['user_id'])
        mediums = Format.objects.all().values()
        langs = Language.objects.all().values()
        context = {
            'user': user,
            'mediums': mediums,
            'langs': langs,
        }
    return render(request, 'admin/admin.html', context)

def login(request):
    user = User.objects.filter(username = request.POST['username'])
    if user:
        userLogin = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), userLogin.password.encode()):
            request.session['user_id'] = userLogin.id
            return redirect('/theAdmin/')
        messages.error(request, 'Invalid Credentials')
        return redirect('/login/')
    messages.error(request, 'That Username is not in our system, please register for an account')
    return redirect('/login/')

def register(request):
    if request.method == 'GET':
        return redirect('/')
    errors = User.objects.validate(request.POST)
    if errors:
        for err in errors.values():
            messages.error(request, err)
        return redirect('/')
    hashedPw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
    newUser = User.objects.create(
        firstName = request.POST['firstName'],
        lastName = request.POST['lastName'],
        email = request.POST['email'],
        username = request.POST['username'],
        password = hashedPw
    )
    request.session['user_id'] = newUser.id
    return redirect('/theAdmin/')

def logout(request):
    request.session.clear()
    messages.error(request, 'You have been logged out')
    return redirect('/')