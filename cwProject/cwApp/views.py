from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .forms import ContactForm
from .models import Contact
# Create your views here.

def index(request):
    contact_list=Contact.objects.all()
    return render(request,'cwApp/index.html',{'contacts':contact_list})

def createUser(request):   #creates user

    newUser=ContactForm(request.POST or None)
    if newUser.is_valid():   #if form is clean, saves and redirects to index
        newUser.save()
        return redirect('index')

    return render(request,'cwApp/create.html',{'newUser':newUser})   #render on create page

def editUser(request,ID):
        user = get_object_or_404(Contact,pk=ID)    #gets id from user
        editContact=ContactForm(request.POST or None, instance=user)   #uses instance to enable the editing
        if editContact.is_valid():
            editContact.save()
            return redirect('index')
        return render(request,'cwApp/create.html',{'newUser':editContact})   #renders to create page to enable editing

def deleteUser(request,ID):
        user = get_object_or_404(Contact,pk=ID)  #obtains id
        if request.method== 'POST':
            user.delete()    #delets
            return redirect('index')

        return render(request,'cwApp/delete.html',{'deleteUser':user})   #deletes user

def readUser(request,ID):   #obtains id
    user=get_object_or_404(Contact,pk=ID)
    return render(request,'cwApp/read.html',{'readUser':user})  #reads sole individual's information
