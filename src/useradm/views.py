
from django.shortcuts import  get_object_or_404
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied
from .validators import IbanValidator
from .models import CtClient


class CtHome(TemplateView):
    template_name = 'useradm/home.html'


@method_decorator(login_required, name='dispatch')
class CtClientList(ListView):
    paginate_by = 5
    template_name = 'useradm/index.html'
    model = CtClient


@method_decorator(login_required, name='dispatch')
class CtClientCreation(CreateView):
    model = CtClient
    template_name = 'useradm/ctclient_form.html'
    success_url = reverse_lazy('index')
    fields = ['first_name', 'last_name', 'iban']
    validators = {"iban": IbanValidator}

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        instance.save()
        return super().form_valid(form)


class ModificationByOwnerMixin:
    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg, None)
        if pk is not None:
            ct_client = get_object_or_404(CtClient, pk=pk)
            if ct_client.owner.id != self.request.user.id:
                raise PermissionDenied
            return ct_client
        else:
            raise AttributeError(u"Update View %s must be called with "
                                 u"either an object pk or a slug."
                                 % self.__class__.__name__)


@method_decorator(login_required, name='dispatch')
class CtClientUpdate(ModificationByOwnerMixin, UpdateView):
    model = CtClient
    template_name = 'useradm/ctclient_form.html'
    success_url = reverse_lazy('index')
    fields = ['first_name', 'last_name', 'iban']

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        instance.save(update_fields=['first_name', 'last_name', 'iban'])
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class CtClientDelete(ModificationByOwnerMixin, DeleteView):
    model = CtClient
    success_url = reverse_lazy('index')


