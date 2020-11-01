from django.urls import path

from . import views

app_name = 'currencies'
handler404 = 'currencies.views.handler404'
handler500 = 'currencies.views.handler404'
urlpatterns = [
    path('', views.HomeView.as_view())
]
