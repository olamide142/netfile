from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from .forms import UploadFileForm
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import os

# Create your views here.



def join(request):
    form = UploadFileForm()
    username = request.POST.get('username')
    user = authenticate(username=username, password='admin')

    if user is not None:
        login(request, user)

        files = File.objects.all()
        users = User.objects.all()
        context = {'form':form, 'files':files, 'users':users}

        return render(request, 'app/index.html', context)
    else:
        # Creating a user cause i was too lazy to look into sessions
        user = User.objects.create_user(username=username, password="admin")
        user.save()
        # CREATE A FOLDER FOR NEW USER 
        folder = str(user).replace(' ','')
        os.mkdir('static/upload/'+str(folder))
        login(request, user)

        files = File.objects.all()
        users = User.objects.all()
        context = {'form':form, 'files':files, 'users':users}

        return render(request, 'app/index.html', context)




def index(request):
    form = UploadFileForm()

    if request.method == 'POST':

        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():

            file_owner = str(request.user)
            file_size = request.POST.get('filesize')
            file_ext = request.POST.get('file_extension')
            file_name = request.POST.get('file_name')

            file_ = File.objects.create(
                file_owner=file_owner, 
                file_name=file_name,
                file_ext=file_ext,
                file_size=file_size)
            file_.save()

            upload_file = request.FILES['file']
            handle_uploaded_file(request, upload_file)
            
            files = File.objects.all()
            users = User.objects.all()
            context = {'form':form, 'files':files, 'users':users}
            return render(request, 'app/index.html', context)


        else:
            return HttpResponse("ERROR, \nSomething went wrong")

    else:
        files = File.objects.all()
        users = User.objects.all()
        context = {'form':form, 'files':files, 'users':users}
        return render(request, 'app/index.html', context)




def handle_uploaded_file(request, f):
    # Get the users folder by name 
    folder = str(request.user).replace(' ','')
    # Upload file to user folder 
    with open('static/upload/'+str(folder)+'/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def logout_view(request):
    logout(request)
    form = UploadFileForm()
    files = File.objects.all()
    users = User.objects.all()
    context = {'form':form, 'files':files, 'users':users}

    return render(request, 'app/index.html', context)