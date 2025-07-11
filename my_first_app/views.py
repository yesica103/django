from django.shortcuts import render

# Create your views here.
def my_view(request):
    # This is a simple view that renders a template
    car_list = [
        {"title": "Toyota Camry", "year": 2020, "price": 24000},
        {"title": "Honda Accord", "year": 2019, "price": 22000},
        {"title": "Ford Focus", "year": 2018, "price": 18000},
        {"title": "Chevrolet Malibu", "year": 2021, "price": 26000}
    ]
    context = {
        "car_list": car_list
    }
    return render(request, "my_first_app/car_list.html", context)
