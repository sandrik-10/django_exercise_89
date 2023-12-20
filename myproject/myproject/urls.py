
from django.contrib import admin
from django.urls import path
from myproject.views import calculator
urlpatterns = [
    path('admin/', admin.site.urls),
    path('odd_or_even/<int:number>', calculator)
]
