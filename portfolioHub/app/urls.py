from django.urls import path
from app.routes.insert import insert
from app.routes.find import find
from app.routes.find_many import find_many
from app.routes.delete import delete
from app.routes.delete_many import delete_many
from app.routes.insert_many import insert_many

urlpatterns = [
    path('insert/', insert),
    path('insert_many/', insert_many),
    path('find/', find),
    path('find_many/', find_many),
    path('delete/', delete),
    path('delete_many/', delete_many)
]