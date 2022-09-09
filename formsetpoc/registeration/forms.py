from django import forms
from .models import Company


class Home(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('name', 'email',)


class CompanyProfile(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('establish_year', 'founder', 'ceo',)


class System(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('type', 'sys_type', 'project_name', 'system_parameter_one', 'system_parameter_two',)
