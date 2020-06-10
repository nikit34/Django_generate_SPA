from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('logup/', views.logup, name='logup'),
    path('accounts/', include('django.contrib.auth.urls')),

    path('search/', views.searchFilterView, name="search"),
    path('delete_page/<int:pk>/', views.delete_page, name='delete_page'),
    path('pages/', views.PageListView.as_view(), name='page_list'),
    path('page/<slug:slug>/', views.PageDetailView.as_view(), name='detail'),
    path('pages/upload/', views.upload_page, name='upload_page'),
]