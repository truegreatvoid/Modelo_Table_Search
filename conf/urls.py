from django.contrib import admin
from django.urls import path, include  # Certifique-se de importar include aqui

urlpatterns = [
    path('ceo-controler/', admin.site.urls),
    path('', include('table.urls', namespace='table')),
]
