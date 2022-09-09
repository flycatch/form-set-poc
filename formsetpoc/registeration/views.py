from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.list import ListView
from formtools.wizard.views import SessionWizardView

from .forms import Home, CompanyProfile, System
from .models import Company


class FormWizardView(SessionWizardView):
    template_name = "wizard_form.html"
    form_list = [Home, CompanyProfile, System]

    def done(self, form_list, **kwargs):
        model = Company()
        for formvalue in form_list:
            for key, value in formvalue.cleaned_data.items():
                setattr(model, key, value)
        model.save()
        return render(self.request, 'done.html', {
            'form_data': [form.cleaned_data for form in form_list],
        })


class ListProject(ListView):
    model = Company
    template_name = "list.html"


class ListProjectDetailView(DetailView):
    model = Company
    template_name = "project_detail.html"

