from django.shortcuts import render
from .models import PortfolioElement, ServicesElement

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


def portfolio(request):
    portfolio_elements = PortfolioElement.objects.all()
    context = {'text': "Welcome my guest! :D", 'title': "Portfolio",
               'portfolio_elements': portfolio_elements}
    return render(request, 'portfolio.html', context)


def services(request):
    services_elements = ServicesElement.objects.order_by('-order_on_website')
    context = {'text': "Welcome my guest! :D", 'title': "Services",
               'services_elements': services_elements}
    return render(request, 'services.html', context)


def shop(request):
    context = {'text': "Welcome my guest! :D", 'title': "Shop"}
    return render(request, 'shop.html', context)
