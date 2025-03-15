from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home_page'),
    path('about-us', views.about_us, name='about_us'),
    path('popular-questoin', views.popular_question, name='popular_question'),
]