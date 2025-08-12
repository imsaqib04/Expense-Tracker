from django.urls import path
from .views import index,edit,delete

urlpatterns = [

    path("",index,name='index'),
    path("edit/<int:id>/",edit,name="edit"),
    path("delete/<int:id>/",delete,name="delete"),
]
