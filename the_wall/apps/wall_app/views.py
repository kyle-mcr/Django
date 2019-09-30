from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt

def index(request):
    return render(request, "wall_app/index.html")

def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:                
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        print(pw_hash)
        new_user = User.objects.create(first_name=first_name, last_name=last_name, email=email, password=pw_hash)
        new = new_user.id
        request.session['current_user'] = new
        return redirect('/success/{}'.format(new))

def success(request, user_id):
    context = {
        'user': User.objects.get(id=user_id),
        'messages': Message.objects.all().order_by('-created_at'),
        'comments': Comment.objects.all().order_by('-created_at')
    }
    try:
        if request.session['current_user']:
            return render(request, "wall_app/success.html", context)
    except:
        return redirect('/')

def login(request):
    users = User.objects.filter(email=request.POST['email'])
    if users:
        current_user = users[0]
        if bcrypt.checkpw(request.POST['password'].encode(), current_user.password.encode()):  
            request.session['current_user'] = current_user.id
            user = users[0].id
            return redirect('/success/{}'.format(user))
    return redirect('/')

def clear(request):
    session_keys = list(request.session.keys())
    for key in session_keys:
        del request.session[key]
    return redirect('/')

def wall(request, user_id):
    user = User.objects.get(id=user_id)
    Message.objects.create(message=request.POST['message'], author=user)
    return redirect('/success/{}'.format(user_id))

def comment(request, user_id, message_id):
    user = User.objects.get(id=user_id)
    message = Message.objects.get(id=message_id)
    Comment.objects.create(comment=request.POST['comment'], author=user, post=message)
    return redirect('/success/{}'.format(user_id))
