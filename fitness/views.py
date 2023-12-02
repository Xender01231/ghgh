from django.shortcuts import render
import random

# Create your views here.
def index(request):
    return render(request, "fitness/index.html")


    
def magic_number(request):
    if request.method == "POST":
        number = int(request.POST['number'])
        random_number = random.randint(1,10)
        if number == random_number:
            return render(request, "fitness/magic_number.html", {'result': "you win!"})
        else:
            return render(request, "fitness/magic_number.html", {'result': "you lose!"})
    else:
            return render(request, "fitness/magic_number.html",)