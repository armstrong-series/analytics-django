from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Data, Dataset

User = get_user_model()


class Dashboard(TemplateView):
    template_name = 'dashboard/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class Signin(TemplateView):
    template_name = 'authentication/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        data = {
            "sales": 100,
            "customers": 10,
            "users": User.objects.all().count()
        }
        return Response(data)


class AjaxTemplateMixin(object):

    def dispatch(self, request, *args, **kwargs):
        if not hasattr(self, 'ajax_template_name'):
            split = self.template_name.split('.html')
            split[-1] = '_inner'
            split.append('.html')
            self.ajax_template_name = ''.join(split)
        if request.is_ajax():
            self.template_name = self.ajax_template_name
        return super(AjaxTemplateMixin, self).dispatch(request, *args, **kwargs)


class CreateData(AjaxTemplateMixin, SuccessMessageMixin, CreateView):
    model = Data
    fields = ["contaminant_area", "image", "tag"]
    template_name = 'dashboard/data-add.html'
    success_url = reverse_lazy("analytics:dashboard.home")
    success_message = 'Data generated /n successfully!'

    def get_form(self, form_class=None):
        form = super().get_form()
        for field in form.fields:
            form.fields[field].widget.attrs.update({"class": 'form-control'})
            return form
