from django.core.paginator import Paginator
from django.http import JsonResponse
from django.views.generic import ListView
from .models import Person
import logging

logger = logging.getLogger(__name__)


class PersonListView(ListView):
    model = Person
    template_name = 'person_list.html'
    context_object_name = 'people'
    paginate_by = 10  # Quantidade de itens por página

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name', '')
        address = self.request.GET.get('address', '')
        city = self.request.GET.get('city', '')
        state = self.request.GET.get('state', '')
        phone_number = self.request.GET.get('phone_number', '')
        birth_date = self.request.GET.get('birth_date', '')
        occupation = self.request.GET.get('occupation', '')

        if name:
            queryset = queryset.filter(name__icontains=name)
        if address:
            queryset = queryset.filter(address__icontains=address)
        if city:
            queryset = queryset.filter(city__icontains=city)
        if state:
            queryset = queryset.filter(state__icontains=state)
        if phone_number:
            queryset = queryset.filter(phone_number__icontains=phone_number)
        if birth_date:
            queryset = queryset.filter(birth_date__icontains=birth_date)
        if occupation:
            queryset = queryset.filter(occupation__icontains=occupation)
        return queryset

    def get_template_names(self):
        if self.request.htmx:
            return ['_person_list_body.html']
        return [self.template_name]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page_number = self.request.GET.get('page', 1)

        # Log para depuração
        logger.debug(f"Page number received: {page_number}")
        logger.debug(f"Request headers: {self.request.headers}")

        paginator = Paginator(self.get_queryset(), self.paginate_by)
        page_obj = paginator.get_page(page_number)
        context['page_obj'] = page_obj
        return context



        
