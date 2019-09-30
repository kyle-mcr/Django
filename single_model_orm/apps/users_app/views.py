from django.shortcuts import render, HttpResponse, redirect

def index():
    return render(request, "users_app/index.html")
