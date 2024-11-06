from django.urls import path

from . import views

urlpatterns = [
    path('list', views.TarefaListView.as_view(), name='tarefa_list'),
    path('cad', views.TarefaCreateView.as_view(), name='tarefa_create'),
    path('<int:pk>', views.TarefaUpdateView.as_view(), name='tarefa_update'),
    path('<int:pk>/delete', views.TarefaDeleteView.as_view(), name='tarefa_delete'),
]