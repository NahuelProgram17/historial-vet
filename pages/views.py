from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import ClinicalRecord
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

class ClinicalRecordListView(LoginRequiredMixin, ListView):
    model = ClinicalRecord
    template_name = 'pages/clinicalrecord_list.html'
    context_object_name = 'records'

    def get_queryset(self):
        return ClinicalRecord.objects.filter(owner=self.request.user)


class ClinicalRecordDetailView(LoginRequiredMixin, DetailView):
    model = ClinicalRecord
    template_name = 'pages/clinicalrecord_detail.html'

    def get_queryset(self):
        return ClinicalRecord.objects.filter(owner=self.request.user)


class ClinicalRecordCreateView(LoginRequiredMixin, CreateView):
    model = ClinicalRecord
    fields = ['pet_name',
    'age',
    'species',
    'clinical_history',
    'rabia', 'rabia_doses',
    'moquillo', 'moquillo_doses',
    'parvovirus', 'parvovirus_doses',
    'image']
    template_name = 'pages/clinicalrecord_form.html'
    success_url = reverse_lazy('pages:list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        messages.success(
            self.request,
            '✅ Historial creado correctamente.'
        )
        return super().form_valid(form)


class ClinicalRecordUpdateView(LoginRequiredMixin, UpdateView):
    model = ClinicalRecord
    fields = ['pet_name',
    'age',
    'species',
    'clinical_history',
    'rabia', 'rabia_doses',
    'moquillo', 'moquillo_doses',
    'parvovirus', 'parvovirus_doses',
    'image']
    template_name = 'pages/clinicalrecord_form.html'
    success_url = reverse_lazy('pages:list')

    def form_valid(self, form):
        messages.success(
            self.request,
            '✏️ Historial actualizado correctamente.'
        )
        return super().form_valid(form)



class ClinicalRecordDeleteView(LoginRequiredMixin, DeleteView):
    model = ClinicalRecord
    template_name = 'pages/clinicalrecord_confirm_delete.html'
    success_url = reverse_lazy('pages:list')

    def delete(self, request, *args, **kwargs):
        messages.warning(
            self.request,
            '🗑️ Historial eliminado.'
        )
        return super().delete(request, *args, **kwargs)
    
@login_required
def dashboard(request):
    return render(request, 'pages/dashboard.html')