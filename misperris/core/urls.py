from django.contrib import admin
from django.conf import settings
from django.urls import path,include
from .views import index,formulario,intermedio,listar,eliminar,modificar,formularioS,eliminarS,listarS,loginM,logoutM,error_accesoM, loginS, logoutS, asignar, listarAdop, listarDisp, listarAsig
urlpatterns = [
    path('',index,name='home'),    
    path('intermedio/',intermedio,name='intermedio' ),
    path('formularioM/',formulario,name='forM'),
    path('listarM/',listar,name='listM'),
    path('eliminarM/',eliminar,name='eliM'),
    path('modificarM/',modificar,name='modM'),
    path('formularioS/',formularioS,name='forS'),
    path('eliminarS/',eliminarS,name='eliS'),
    path('listarS/',listarS,name='listS'),
    path('loginM',loginM,name='logM'),
    path('logoutM/',logoutM,name='logoutM'),
    path('accounts/login/',error_accesoM,name='errorM'),
    path('loginS/', loginS, name='logS'),
    path('logoutS/',logoutS, name='logoutS'),
    path('asignarM/', asignar,name='asigM'),
    path('listarMD/', listarDisp, name='dispM'),
    path('listarMA/', listarAdop, name='adopM'),
    path('listarSM/', listarAsig, name='masado'),
    path('formularioS2/', formularioS, name='forS2')

  

]


