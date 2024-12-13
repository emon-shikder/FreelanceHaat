from django import forms
from .models import Job, Proposal

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ('title', 'description', 'budget', 'deadline', 'skills_required')
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date'}),
        }

class ProposalForm(forms.ModelForm):
    class Meta:
        model = Proposal
        fields = ('cover_letter', 'bid_amount')