from django.urls import path
from django.contrib import admin
#now import the views.py file into this code
from . import views

urlpatterns=[
  path('',views.index),
  path("admin/", admin.site.urls),
  path('home/',views.home_view),
  path('formsets/',views.formset_view),
  path('modelformsets/', views.formset_model),
  path('templateview/', views.geeks_view),
  path('templateviewdate/', views.geeks_templ_view1),
  path('listview/', views.list_view),
  path('listviewclass/', views.GeeksList.as_view()),
  path('create/', views.create_view),
  path('table/<id>', views.detail_view ),
  path('table/<id>/update', views.update_view),
  path('table/<id>/delete', views.delete_view),
]