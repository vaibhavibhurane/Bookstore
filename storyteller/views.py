from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from storyteller.models import Info, User


def index(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())


def second(request):
    template = loader.get_template('registration.html')
    return HttpResponse(template.render({}, request))


def third(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render({}, request))


def data(request):
    mymembers = Info.objects.all().values()
    template = loader.get_template('data.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))


def add(request):
    template = loader.get_template("add.html")
    return HttpResponse(template.render({}, request))


def addrecord(request):
    x = request.POST['bookname']
    y = request.POST['author']
    z = request.POST['isbn']
    w = request.POST['price']
    member = Info(bookname=x, author=y, isbn=z, price=w)
    member.save()
    return HttpResponseRedirect(reverse('data'))


def user(request):
    d = request.POST['username']
    f = request.POST['password']
    member = User(username=d, password=f)
    member.save()
    return HttpResponseRedirect(reverse('index'))


def sell(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))


def gallery(request):
    template = loader.get_template('gallery.html')
    return HttpResponse(template.render({}, request))


def about(request):
    template = loader.get_template('aboutus.html')
    return HttpResponse(template.render({}, request))


def purchase(request):
    template = loader.get_template('purchase.html')
    return HttpResponse(template.render({}, request))


def order(request):
    template = loader.get_template('order.html')
    return HttpResponse(template.render({}, request))
