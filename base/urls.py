from django.urls import path
from . import views

app_name = "base"

urlpatterns = [
    path('', views.home, name="home"),
    path('project/<str:pk>/', views.projectPage, name="project"),
    path('add-project/', views.addProject, name="add-project"),
    path('edit-project/<str:pk>/', views.editProject, name="edit-project"),
    path('inbox/', views.inboxPage, name="inbox"),
    path('inbox/<str:pk>/', views.messagePage, name="message"),
    path('add_skill/', views.addSkill, name="add-skill"),
    path('add_endorsement/', views.addEndorsement, name="add-endorsement"),
    path('contact/', views.contact, name='contact'),

]
