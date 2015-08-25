from django import http

def home(request):
    return http.HttpResponse('Hi Peter, Hello World!, again')
