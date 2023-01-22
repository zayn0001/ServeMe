from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import DinerLogin, ManagerLogin
from django.contrib.auth import login, authenticate
from .models import Diner, Manager, Layout, Menu, FoodItem
from django.contrib.auth.models import User
import json

# Create your views here.
def front(request):
    return render(request, "selection.html")

def diner(request):
    return render(request, "dinersign.html")

def manager(request):
    return render(request, "managersign.html")


def dinerregister(request):				 
    if request.method == "POST":
        form = DinerLogin(request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect("/diner/")
        return render(request, 'dinerregister.html', {'error' : 'There is already an account with this username.'})
    return render (request=request, template_name="dinerregister.html")

def dinerlogin(request):
    if request.method == 'POST':
        print(request.POST)

        #change
        form = DinerLogin(request.POST)
        print(form.errors)
        #print(form)

        username = request.POST["username"]
        password = request.POST['password']
        try:
            if Diner.objects.get(username=username):
                if password == Diner.objects.get(username=username).password:
                    return redirect('/diner/scan')
        except:
            return render(request, 'dinerlogin.html', {'error' : 'username or password is incorrect.'})
    return render(request, 'dinerlogin.html')


def scan(request):
    return render(request, 'qrcodescanner.html')

def managerregister(request):				 
    if request.method == "POST":
        form = ManagerLogin(request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect("/diner/")
        return render(request, 'managerregister.html', {'error' : 'There is already an account with this username.'})
    return render (request=request, template_name="managerregister.html")

def managerlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if Manager.objects.get(username=username):
            if password == Manager.objects.get(username=username).password:
                request.session["loggedin"] = True
                return redirect('managerprofile', username)

        return render(request, 'managerlogin.html', {'error' : 'username or password is incorrect.'})
    return render(request, 'managerlogin.html')

def managerprofile(request, managername):

    if request.META.get('HTTP_REFERER') and "/manager/login" in request.META.get('HTTP_REFERER'):
        return render(request, 'managerprofile.html' ,{"managername":managername})
    return redirect('managerlogin')

def createfloor(request, managername):
    if request.method == "POST":
        tables = request.POST["tables"]
        name = request.POST["name"]
        manager = Manager.objects.get(username=managername)
        print(tables)
        print(request.POST)
        layout = Layout(manager=manager, plan=tables, name=name)
        layout.save()   
        return render(request, 'managerprofile.html', {"managername":managername})
    return render(request, 'createfloor.html', {"managername":managername})

def layouts(request, managername):
    manager = Manager.objects.get(username=managername)
    plan = Layout.objects.get(manager=manager).plan
    plan = json.loads(plan)
    #print(plan)
    return render(request, 'profilefloors.html', {"managername":managername, "plan":json.dumps(plan["plan"]), "numRows":plan["numRows"], "numCols":plan["numCols"]}) 

def menu(request, managername):
    manager = Manager.objects.get(username=managername)
    menu = Menu.objects.get(manager=manager)
    menulist = {}
    count = 0
    for items in FoodItem.objects.filter(menu=menu):
        menulist[count] = {}
        menulist[count]["name"] = items.name
        menulist[count]["price"] = str(items.price)
        menulist[count]["description"] = items.description
        count = count+1
    return render(request, 'profilemenu.html', {"managername":managername, "menu":json.dumps(menulist)})

def createmenu(request, managername):
    if request.method=="POST":
        manager = Manager.objects.get(username=managername)
        name = request.POST["name"]
        price = request.POST["price"]
        description = request.POST["description"]
        if  not Menu.objects.get(manager=manager):
            menu = Menu(manager=manager)
            menu.save()
        else:
            menu = Menu.objects.get(manager=manager)
        item = FoodItem(menu=menu, name=name, price=price, description=description)
        item.save()
        return render(request, 'managerprofile.html', {"managername":managername})
    #manager = Manager.objects.get(username=managername)
    #menu = Layout.objects.get(manager=manager).menudata
    return render(request, 'createmenu.html', {"managername":managername})
