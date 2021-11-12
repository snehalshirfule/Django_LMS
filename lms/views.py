from django.shortcuts import render,redirect
from lms.forms import *
from lms.forms import BookRecordForm
from lms.models import books,lms_admin

# Create your views here.
def signin(request):
    if request.method == "POST":
        print("form submit--------------------------------")
        form = AdminSigninForm(request.POST)
        if form.is_valid():
            print('form valid--------------------')
            email = request.POST["email"]
            password = request.POST["password"]
            try:
                result = lms_admin.objects.get(
                    email=email, password=password)
                if result:
                    print(result.id)
                    request.session['email']=result.id
                    request.session['name']=result.name
                    return redirect("/showbooks")
            except lms_admin.DoesNotExist:
                message = "Invalid email or password"
                return render(request, "signin.html", {'message': message})
                     
    else:
                     
        return render(request,'signin.html')

def signup(request):
    if request.method == "POST":
        print('signup form---------------------------------------------')
        form = AdminSignupForm(request.POST)
        email=request.POST["email"]
        if form.is_valid():
            try:
               if lms_admin.objects.get(email=email):
                    message="User already Exists"
                    return render(request,'signup.html',{'message':message})
            except lms_admin.DoesNotExist:
                form.save()
                return redirect('/signin')
    return render(request,'signup.html')


def addbook(request):
    if 'email' in request.session:          
        if request.method == "POST":  
            print('form submit--------------------------------------------')
            form = BookRecordForm(request.POST)
            if form.is_valid():
                    print('form valid---------------------------')
            try:  
                form.save()  
                return redirect('/showbooks') 
                # return render(request,'showbooks.html')
            except:  
                return render(request,'addbook.html') 
            else:
                print('Else -----------------------------------')
                print(form.errors.as_data())
                return render(request,'addbook.html')

        else:
            return render(request,'addbook.html')
    else:
        return redirect('/signin')

def showbooks(request):
    if 'email' in request.session:        
        bookData = books.objects.all()  
        return render(request,'showbooks.html',{'books':bookData})

    else:
        return redirect('/signin')

def destroy(request, id):
    if 'email' in request.session :  
        booksData = books.objects.get(id=id)  
        booksData.delete()  
        return redirect("/showbooks") 
    else:
        return redirect('/signin')

def edit(request, id):  
    if 'email' in request.session :
        bookData = books.objects.get(id=id)  
        return render(request,'update.html', {'Books':bookData}) 
    else:
        return redirect('/signin') 
def update(request,id):
    if 'email' in request.session :  
        bookData = books.objects.get(id=id)  
        form = BookRecordForm(request.POST, instance = bookData)  
        if form.is_valid():  
            form.save()  
            return redirect("/showbooks") 
        else:
            print(form.errors) 
        return render(request, 'update.html', {'books': bookData})
    else :
        return redirect('/signin') 


def recordsofbook(request):
    bookData = books.objects.all()
    return render(request,'records.html',{'books':bookData})


def signout(request):
    if 'email' in request.session :
        try:
            del request.session['email']
            return redirect('/signin')
        except:
            pass

    