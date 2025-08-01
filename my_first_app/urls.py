"""
URL configuration for my_first_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.http import HttpResponse
from django.urls import path
from my_first_app.views import author_profile_view, my_view, my_test_view, CarListView



urlpatterns = [
    #path("listado/", my_view),
    path("listado/", CarListView.as_view()),
    path("detalle/<int:id>", my_test_view),
    path("marcas/<str:brand>", my_test_view),
    path("author-profile/<int:id>", author_profile_view),

]
