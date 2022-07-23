from django.urls import path
from . import views

urlpatterns = [

    path('api/show_classrooms/<status>/', views.ClassroomList.as_view(),
         name="show_classrooms"),
    path('api/show_faculty/<status>/', views.FacultyList.as_view(),
         name="show_classrooms")
]