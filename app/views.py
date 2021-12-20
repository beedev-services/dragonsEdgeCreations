from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt

# ---------- Index ----------

def index(request):
    return render(request, "index.html")

# ---------- About ----------

def about(request):
    currentEvents = Event.objects.filter(eventStatus=0).order_by('date')
    pastEvents = Event.objects.filter(eventStatus=1).order_by('-date')
    context = {
        'currentEvents': currentEvents,
        'pastEvents': pastEvents,
    }
    return render(request, 'about.html', context)

# ---------- Books ----------
def books(request):
    books = Product.objects.filter(prodType=0).order_by('prodName')
    context = {
        'books': books,
    }
    return render(request, 'books.html', context)

# ---------- Art ----------
def art(request):
    arts = Product.objects.filter(prodType=1).order_by('prodName')
    context = {
        'arts': arts,
    }
    return render(request, 'art.html', context)

def uc(request):
    return render(request, 'uc.html')

# ---------- Services ----------
def services(request):
    return render(request, 'services.html')

# ---------- Contact ----------
def contact(request):
    return render(request, 'contact.html')

# ---------- Admin ----------
def theAdminLogin(request):
    context = {
        'user': User.objects.all().values()
    }
    return render(request, 'admin/theLogin.html', context)

def theAdminSignup(request):
    user = User.objects.filter(username = request.POST['username'])
    if user:
        userLogin = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), userLogin.password.encode()):
            request.session['user_id'] = userLogin.id
            return redirect('/theAdmin/')
        messages.error(request, 'Invalid Credentials')
        return redirect('/theAdmin/login/')
    messages.error(request, 'That Username is not in our system, please register for an account')
    return redirect('/theAdmin/login/')

def theAdminRegister(request):
    if request.method == 'GET':
        return redirect('/theAdmin/login/')
    errors = User.objects.validate(request.POST)
    if errors:
        for err in errors.values():
            messages.error(request, err)
        return redirect('/theAdmin/login/')
    hashedPw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
    newUser = User.objects.create(
        firstName = request.POST['firstName'],
        lastName = request.POST['lastName'],
        email = request.POST['email'],
        adminKey = request.POST['adminKey'],
        username = request.POST['username'],
        password = hashedPw
    )
    request.session['user_id'] = newUser.id
    return redirect('/theAdmin/')

def theAdmin(request):
    if 'user_id' not in request.session:
        messages.error(request, 'Please Log in to view')
        return redirect('/theAdmin/login/')
    else:
        user = User.objects.get(id=request.session['user_id'])
        mediums = Format.objects.all().values()
        langs = Language.objects.all().values()
        context = {
            'user': user,
            'mediums': mediums,
            'langs': langs,
        }
    return render(request, 'admin/theAdmin.html', context)

def logout(request):
    request.session.clear()
    messages.error(request, 'You have been logged out')
    return redirect('/')

def createEvent(request):
    Event.objects.create(
        eventName=request.POST['eventName'],
        date=request.POST['date'],
        details=request.POST['details'],
        location=request.POST['location'],
        eventStatus=request.POST['eventStatus'],
    )
    messages.error(request, "Event Added")
    return redirect('/theAdmin/events/')

def createFormat(request):
    Format.objects.create(
        medium=request.POST['medium'],
    )
    messages.error(request, "Format Added")
    return redirect('/theAdmin/')

def createLang(request):
    Language.objects.create(
        lang=request.POST['lang'],
    )
    messages.error(request, "Language Added")
    return redirect('/theAdmin/')

def createProd(request):
    Product.objects.create(
        prodName=request.POST['prodName'],
        prodDetails=request.POST['prodDetails'],
        author=request.POST['author'],
        illustrator=request.POST['illustrator'],
        isbn=request.POST['isbn'],
        quantity=request.POST['quantity'],
        prodPrice=request.POST['prodPrice'],
        prodType=request.POST['prodType'],
        prodMedium_id=request.POST['prodMedium'],
        prodLang_id=request.POST['prodLang'],
    )
    messages.error(request, "Item Created You can now add an Image")
    return redirect('/theAdmin/products/')

def theAdminAllProds(request):
    if 'user_id' not in request.session:
        messages.error(request, "Please log in or See Webmaster")
        return redirect('theAdmin/login/')
    else:
        user = User.objects.get(id=request.session['user_id'])
        product = Product.objects.all().values()
        medium = Format.objects.all().values()
        language = Language.objects.all().values()
        context = {
            'user': user,
            'product': product,
            'medium': medium,
            'language':language,
        }
        return render(request, 'admin/allProds.html', context)

def theAdminAllEvents(request):
    if 'user_id' not in request.session:
        messages.error(request, "Please log in or see Webmaster")
        return redirect('theAdmin/login/')
    else:
        user = User.objects.get(id=request.session['user_id'])
        events = Event.objects.all().values()
        context = {
            'user': user,
            'events': events,
        }
        return render(request, 'admin/allEvents.html', context)

def theAdminViewEvent(request, event_id):
    if 'user_id' not in request.session:
        messages.error(request, "Please log in or see Webmaster")
        return redirect('theAdmin/login/')
    else:
        user = User.objects.get(id=request.session['user_id'])
        event = Event.objects.get(id=event_id)
        context = {
            'user': user,
            'event': event,
        }
        return render(request, 'admin/viewEvent.html', context)

def theAdminViewProd(request, product_id):
    if 'user_id' not in request.session:
        messages.error(request, "Please log in or see Webmaster")
        return redirect('theAdmin/login/')
    else:
        user = User.objects.get(id=request.session['user_id'])
        prod = Product.objects.get(id=product_id)
        medium = Format.objects.all().values()
        language = Language.objects.all().values()
        context = {
            'user': user,
            'prod': prod,
            'medium': medium,
            'language':language,
        }
        return render(request, 'admin/viewProd.html', context)

def updateProd(request, product_id):
    toUpdate = Product.objects.get(id=product_id)
    toUpdate.prodName = request.POST['prodName']
    toUpdate.prodDetails = request.POST['prodDetails']
    toUpdate.author = request.POST['author']
    toUpdate.illustrator = request.POSt['illustrator']
    toUpdate.quantity = request.POST['quantity']
    toUpdate.prodPrice = request.POST['prodPrice']
    toUpdate.prodType = request.POSt['prodType']
    toUpdate.prodMedium = request.POSt['prodMedium']
    toUpdate.prodLang = request.POST['prodLang']
    toUpdate.save()
    return redirect('/theAdmin/allProds/')