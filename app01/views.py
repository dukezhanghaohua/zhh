from django.shortcuts import render

# Create your views here.
def hello(request):
    print('request is :',request)
    return HttpResponse('django is ok ')
