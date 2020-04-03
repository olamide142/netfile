from .forms import UploadFileForm
from .models import *

from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse, FileResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt

import os
import random
from zipfile import ZipFile
# Create your views here.



def join(request):
    form = UploadFileForm()
    username = request.POST.get('username').lower().strip()
    user = authenticate(username=username, password='admin')

    if user is not None:
        login(request, user)

        context = return_context(request.user)
        return render(request, 'app/index.html', context)
    else:
        # Creating a user cause i was too lazy to look into sessions
        user = User.objects.create_user(username=username, password="admin")
        user.save()
        # CREATE A FOLDER FOR NEW USER 
        folder = str(user).replace(' ','')
        os.mkdir('static/upload/'+str(folder))
        login(request, user)

        context = return_context(request.user)
        return render(request, 'app/index.html', context)


def index(request):

    context = return_context(request.user)
    return render(request, 'app/index.html', context)


def upload(request):
    if request.method == "POST":

        form = UploadFileForm(request.POST, request.FILES)

        if True:

            file_owner = str(request.user)
            file_size = request.POST.get('file_size')
            file_ext = request.POST.get('file_extension')
            file_name = request.POST.get('file_name')

            file_ = File.objects.create(
                file_owner=file_owner, 
                file_name=file_name,
                file_ext=file_ext,
                file_size=file_size,
                file_id = generate_file_id())
            file_.save()


            upload_file = request.FILES['file']
            handle_uploaded_file(request, upload_file)
            
            context = return_context(request.user)
            return render(request, 'app/index.html', context)

        else:
            return JsonResponse({'file_id': "Something went wrong"})


def handle_uploaded_file(request, f):
    # Get the users folder by name 
    folder = str(request.user).replace(' ','')
    # Upload file to user folder 
    with open('static/upload/'+str(folder)+'/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def download_file(request):
    file_id = request.POST.get('x')
    file = File.objects.get(file_id=file_id)
    folder = str(file.file_owner).replace(' ','')
    ext = str(file.file_ext)
    file = str(file.file_name) +'.'+ext

    # for some weird reasons mp4 files won't download with FileResponse 
    # So follow the other way 🤷‍♂️🤷‍♂️🤷‍♂️🤷‍♀️🤷‍♀️🤷‍♀️
    if ext.lower() != "mp4":
        return FileResponse(open('static/upload/'+str(folder)+'/'+file, 'rb'))

    with open('static/upload/'+str(folder)+'/'+file, 'rb') as ext:
        response = HttpResponse(ext.read())
        response['content_type'] = 'application/'+str(ext)
        response['Content-Disposition'] = 'attachment;filename='+file
        return response


def delete_file(request):
    folder = str(request.user).replace(' ','')
    file_id = request.POST.get('xx')
    file = File.objects.get(file_id=file_id)
    ext = str(file.file_ext)
    file_ = str(file.file_name) +'.'+ext
    file.delete() 

    os.remove('static/upload/'+str(folder)+'/'+file_)
    context = return_context(request.user)
    return render(request, 'app/index.html', context)



def logout_view(request):
    logout(request)
    context = return_context(request.user)
    return render(request, 'app/index.html', context)


def return_context(user):
    form = UploadFileForm()
    files = File.objects.all()
    users = User.objects.all()
    logged_in = File.objects.filter(file_owner = user)
    context = {'form':form, 'files':files, 'users':users, 'logged_in':logged_in}

    return context 


def generate_file_id():
    data = "QWERTYUIOPLKJHGFDSAZXCVBNMqwertyuioplkjhgfdsazxcvbnm1234567890"
    file_id = ""
    for i in range(10):
        file_id += random.choice(data)
    return file_id




def debugMode():
    print("FORM IS VALID")
    print("FORM IS VALID")
    print("FORM IS VALID")
    print("FORM IS VALID")
    print("FORM IS VALID")
    print("FORM IS VALID")
    print("FORM IS VALID")
    print("FORM IS VALID")
    print("FORM IS VALID")
    print("FORM IS VALID")
    print("FORM IS VALID")
    print("FORM IS VALID")
    print("FORM IS VALID")
    print("FORM IS VALID")
    print("FORM IS VALID")
    print("FORM IS VALID")
    print("FORM IS VALID")
    print("FORM IS VALID")
    print("FORM IS VALID")
    print("FORM IS VALID")
    print("FORM IS VALID")
    print("FORM IS VALID")
    print("FORM IS VALID")
    print("FORM IS VALID")