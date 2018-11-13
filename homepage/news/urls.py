from django.urls import path,include
from . import views

app_name = 'news'

urlpatterns = [
    path('',views.TemplateView.as_view(),name="top"),
    path("news/",views.IndexView.as_view(),name="index"),
    path("news/category/<int:pk>/",views.CategoryView.as_view(),name="category"),
    path("news/detail/<int:pk>/",views.DetailView.as_view(),name="detail"),
    # path()
]
