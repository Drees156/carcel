from django.urls import path
from .views import home, user_login, user_logout, registrarPpl, edicionPpl, editarPpl, eliminarPpl


urlpatterns = [
    path('', user_login, name='login'),
    path('home/', home, name='home'), 
    path('logout/', user_logout, name='logout'),
    path('registrarPpl/', registrarPpl, name='registrarPpl'),
    path('edicionPpl/<nu>/', edicionPpl, name='edicionPpl'),
    path('editarPpl/', editarPpl, name='editarPpl'),
    path('eliminarPpl/<nu>/', eliminarPpl, name='eliminarPpl'),
    
]
