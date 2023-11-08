from django.urls import path

from . import views

urlpatterns = [
    path("sdt", views.sdt, name="sdt"),
    path("show/", views.show, name="show"),
    path("edit/<int:id>", views.edit, name="edit"),
    path("update/<int:id>", views.update, name="update"),
    path("delete/<int:id>", views.destroy, name="destroy"),
]