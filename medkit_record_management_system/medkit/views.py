from django.shortcuts import redirect, render, get_object_or_404
from .models import Information
from .forms import Medkit_Information, Sale_Information, Add_Information
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import date, timedelta





# Landing Page
def home(request):
    return render(request, "home.html")


# Sign up page
def create(request):
    try:
        if request.method == "POST":
            username = request.POST['username']
            fname = request.POST['fname']
            lname = request.POST['lname']
            email = request.POST['email']
            pass1 = request.POST['pass1']
            pass2 = request.POST['pass2']

            myuser = User.objects.create_user(username, email, pass1)
            myuser.first_name = fname
            myuser.last_name = lname

            myuser.save()


            messages.success(
                request, "Staff is successfully registered!")
    except:
        messages.error(request, "Username is already taken!")
        return redirect('createpage')

    return render(request, "signup.html")


# Login page
def signin(request):
    try:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                
                messages.success(request, "welcome to Medkit Record management System!")
                return redirect("/")
            else:
                messages.error(request, "Username or password doesn't exist!")
    except:
        messages.error(request, "Invalid Information")

    return render(request, "login.html")




# Function: Form to add Medkits
@login_required
def addMedkit(request):
    if request.method == 'POST':
        addM = Medkit_Information(request.POST)
        if addM.is_valid():
            messages.success(request, "Medkit was successfully added.")
            addM.save()
            addM = Medkit_Information()
    else:
        addM = Medkit_Information()

    return render(request, "addMedkitForm.html", {'form': addM})


#Function to show expired medkits
@login_required
def expiring_medkits(request):
    today = date.today()
    days_until_expiration = 30

    expiry_date_range = (today + timedelta(days=1), today + timedelta(days=days_until_expiration))
    expiring_objects = Information.objects.filter(expiry_date=expiry_date_range)
    return render(request, 'expiring.html', {'expiring':expiring_objects})


# Function to view
@login_required
def display_data(request):
    total_records = Information.objects.count()
    viewmed = Information.objects.all().order_by('expiry_date')
    if request.method == 'GET':
        st = request.GET.get('servicename')
        if st != None:
            viewmed = Information.objects.filter(medicine_name=st)

    return render(request, "viewMedkit.html", {'viewmed': viewmed, 'total_records': total_records})


# Function to update or edit data
@login_required
def update_data(request, id):
    if request.method == 'POST':
        up = Information.objects.get(pk=id)
        addM = Medkit_Information(request.POST, instance=up)
        if addM.is_valid():
            addM.save()
            messages.success(request, "Medkit was successfully updated!")
    else:
        up = Information.objects.get(pk=id)
        addM = Medkit_Information(instance=up)
        messages.error(request, "Invalid info!")

    return render(request, "updateMedkit.html", {'form': addM})


# Funtion to delete data
@login_required
def delete_data(request, id):
    deletquery = Information.objects.get(pk=id)
    if request.method == 'POST':
        deletquery.delete()
        messages.info(request, "Successfully deleted!")
        return redirect('/displaydata')
    return render(request, "deleteitems.html")


# Function to sale medkit
def salepage(request, id):
    medicine = get_object_or_404(Information, pk=id)
    if request.method == "POST":
       form = Sale_Information(request.POST)
       if form.is_valid():
           quantity = form.cleaned_data['quantity']
           if quantity <= medicine.quantity:
               medicine.quantity -= quantity
               medicine.save()
               messages.success(request, "Successfully sold!")
           else:
               messages.warning(request, "Out of stock")
    else:
        form = Sale_Information()
    return render(request, "sale.html", {'medicine':medicine, 'form':form})

# Function to add quantity of medicines
def addpage(request, id):
    medicine = get_object_or_404(Information, pk=id)
    if request.method == "POST":
       form = Add_Information(request.POST)
       if form.is_valid():
           quantity = form.cleaned_data['quantity']
           if quantity <= medicine.quantity:
               medicine.quantity += quantity
               medicine.save()
               messages.success(request, "Successfully added!")
    else:
        form = Sale_Information()
    return render(request, "add.html", {'medicine':medicine, 'form':form})


#Function to logout
def logout_view(request):
    logout(request)
    return redirect("/")




