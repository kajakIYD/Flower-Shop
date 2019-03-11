from django.shortcuts import render


# Create your views here.


def about(request):
    context = {'text': "Welcome my guest! :D", 'title': "About"}
    return render(request, 'about.html', context)


def blog(request):
    context = {'text': "Welcome my guest! :D", 'title': "Blog"}
    return render(request, 'blog.html', context)


def contact(request):
    context = {'text': "Welcome my guest! :D", 'title': "Contact"}
    return render(request, 'contact.html', context)


def index(request):
    context = {'text': "Welcome my guest! :D", 'title': "Home"}
    return render(request, 'index.html', context)


def services(request):
    context = {'text': "Welcome my guest! :D", 'title': "Services"}
    return render(request, 'services.html', context)


def shop(request):
    context = {'text': "Welcome my guest! :D", 'title': "Shop"}
    return render(request, 'shop.html', context)
