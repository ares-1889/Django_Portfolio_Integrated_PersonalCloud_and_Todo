from django.shortcuts import render
import json
from django.http import JsonResponse
from .models import Users
from .forms import FileUploadForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

def index(request):
    return render(request, 'home.html')

@login_required
def vault(request):
    return render(request, 'vault.html')

@login_required
def route(request):
    return render(request, 'router_page.html')

@login_required
def todo(request):
    return render(request, 'todo.html')


@csrf_exempt
def validate_credentials(request):
    print(Users.objects.all())
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        user = authenticate(request,username=username, password=password)


        try:
            user = Users.objects.get(username=username)
            if user.password == password:
                login(request, user)
                return JsonResponse({'status': 'success'})
            else:
                return JsonResponse({'status': 'error'})
        except Users.DoesNotExist:
            return JsonResponse({'status': 'error'})
    return JsonResponse({'status': 'error'})

@csrf_exempt
def file_upload(request):
    if request.method == 'POST':
        print('Post request recieved')
        print('FILES:', request.FILES)
        print('POST Data:', request.POST)
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            print('Form is valid')
            form.save()
            return JsonResponse({'status': 'success'})
        else:
            print('Form is not valid')
            print('Errors:', form.errors)
            context = {'form': form}

    context = {'form': FileUploadForm()}           
    return JsonResponse({'status': 'fail'})

