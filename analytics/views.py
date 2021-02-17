from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import TemplateView


class Dashboard(TemplateView):
    template_name = 'dashboard/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


