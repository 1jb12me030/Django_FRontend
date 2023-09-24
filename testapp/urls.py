from django.urls import path
from . import views
from .views import CreateStudentView

urlpatterns = [
    path('student_registration/', views.student_registration, name='student_registration'),
    path('test/', views.home, name='home'),
   # path('', views.student_dashboard, name='student_dashboard'),# Define the URL pattern for the home page
    # Add other URL patterns if needed
    path('student_login/', views.student_login, name='student_login'),
    path('update-profile/', views.update_profile, name='update_profile'),
    path('api/create-student/', CreateStudentView.as_view(), name='create-student'),
    #path('profile/', views.student_profile, name='profile'),
    path('update-profile1/', views.update_profile1, name='update-profile1'),
   


]
