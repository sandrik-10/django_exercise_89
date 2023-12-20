from django.http import HttpResponse

def calculator(request, number):
    if int(number) % 2 == 0:
        return HttpResponse("<h1>this number is even</h1>")
    else:
        return HttpResponse("<h1>this number is odd</h1>")