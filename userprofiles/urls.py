from django.urls import path

from userprofiles import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('profile/create/', views.CreateProfileView.as_view()),
    path('profile/<int:pk>/',
         views.RetrieveUpdateDestroyProfileView.as_view()),
]
