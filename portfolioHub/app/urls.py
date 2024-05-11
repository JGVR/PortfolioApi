from django.urls import path
from app.routes.insert import insert
from app.routes.find import find

urlpatterns = [
    path('insert/', insert),
    path('find/', find)
]