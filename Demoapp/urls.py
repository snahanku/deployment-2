from django.contrib import admin
from django.urls import path , include
from Demoapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("new/" , views.hello , name="hello")
]
