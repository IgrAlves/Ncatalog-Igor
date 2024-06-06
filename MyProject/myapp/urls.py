from django.urls import path
from myapp.views import *

# Create your views here.

urlpatterns = [
    path("", index, name="index"),
    path("produto/cadastrar/", create, name="adicionar_item"),
    path("produto/editar/<int:id>", edit, name="editar_item"),
    path("produto/atualizar/<int:id>", update, name="atualizar_item"),
    path("produto/visualizar/<int:id>", read, name="visualizar_item"),
    path("produto/deletar/<int:id>", delete, name="deletar_item"),
    path("produto/listar/", listar, name="listar_item"),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/', signup_view, name='signup'),
]