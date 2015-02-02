from django.shortcuts import HttpResponse


def page(request):
    return HttpResponse("Hello World!")