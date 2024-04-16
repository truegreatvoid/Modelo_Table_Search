from django.urls import path
from .views import PersonListView

app_name = 'table'

urlpatterns = [
    path('', PersonListView.as_view(), name='person_list'),
    # Adicione mais padrões de URL aqui
]
