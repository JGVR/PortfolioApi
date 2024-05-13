from django.urls import path
from app.routes.insert import insert
from app.routes.find import find
from app.routes.find_many import find_many
from app.routes.delete import delete
from app.routes.delete_many import delete_many

urlpatterns = [
    path('insert/', insert),
    path('find/', find),
    path('find_many/', find_many),
    path('delete/', delete),
    path('delete_many/', delete_many)
]