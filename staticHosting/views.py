from django.http import HttpResponse

def helloView(request,name):
    return HttpResponse('Welcome {}'.format(name))