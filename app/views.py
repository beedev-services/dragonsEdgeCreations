from django.shortcuts import render, redirect
from django.contrib import messages
from .defaultData import *

# ----------------------------------- Unprotected Pages -----------------------------------

# ------------------------- Main Landing Pages -------------------------

# ---------- Index ----------

def index(request):
    return render(request, "index.html")

# ---------- About ----------

def about(request):
    noEvents = "Currently, we do not have shows scheduled. Stay tuned!"
    # currentEvents = events
    # pastEvents = pastEvents
    context = {
        'nullEvents': noEvents,
        'events': currentEvents,
        'pastEvents': pastEvents,
    }
    print(currentEvents)
    print(pastEvents)
    return render(request, 'about.html', context)

# ---------- Books ----------
def books(request):
    context = {
        'books': theBooks,
    }
    print(theBooks)
    return render(request, 'books.html', context)

# ---------- Art ----------
def art(request):
    return render(request, 'art.html')

# ---------- Blog ----------
def blog(request):
    return render(request, 'blog.html')

# ---------- Services ----------
def services(request):
    return render(request, 'services.html')

# ---------- Contact ----------
def contact(request):
    return render(request, 'contact.html')

# ---------- Admin ----------
def admin(request):
    return render(request, 'admin.html')

# ------------------------- Landing Pages -------------------------


# ----------------------------------- Protected Pages -----------------------------------

# ------------------------- Create Routes -------------------------

# ---------- Login ----------
def login(request):
    pass

# ---------- Register ----------
def register(request):
    pass

# ---------- Create Book ----------
def createBook(request):
    pass

# ------------------------- Landing Pages -------------------------

# ---------- Login Redirect ----------
def loginPost(request):
    pass

# ---------- Register Redirect ----------
def registerPost(request):
    pass

# ------------------------- Update Routes -------------------------

# ------------------------- Delete Routes -------------------------

# ------------------------- Form Routes -------------------------

