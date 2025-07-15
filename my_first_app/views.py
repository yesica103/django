from django.shortcuts import render
from my_first_app.models import Car, Author, Profile
#from my_first_app.models import Car, Profile
# Create your views here.
def my_view(request):
    # This is a simple view that renders a template
    car_list = Car.objects.all() 
    context = {
        "car_list": car_list
    }
    return render(request, "my_first_app/car_list.html", context)

def author_profile_view(request, *args, **kwargs):
    # This is a simple view that renders a template
    author = Author.objects.get(id=kwargs['id'])
    
    context = {
        "author_profile": author
    }
    return render(request, "my_first_app/author_profile.html", context)

