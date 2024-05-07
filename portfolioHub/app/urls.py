from django.urls import path
from app.routes.insert import insert

urlpatterns = [
    path('insert/', insert)
]