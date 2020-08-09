from django.urls import path
from .views import (
    index,
    add_new,
    update_existing,
    view_data
)

app_name = "handler"

urlpatterns = [
    path('', index, name="index"),
    path('add/', add_new, name="add"),
    path('update/<int:request_id>', update_existing, name="update"),
    path('view/<int:request_id>', view_data, name="view_data"),
]