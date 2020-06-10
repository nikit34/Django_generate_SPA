from django.urls import path

from . import views


urlpatterns = [
    path('create_page/', views.CreatePage.as_view(), name='create_page'),
]