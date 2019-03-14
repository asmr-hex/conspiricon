from django import forms
from .models import RSVP, Presentation


class RSVPForm(forms.ModelForm):
    class Meta:
        model = RSVP
        fields = ('name', 'attending', )
        widgets = {
            'name': forms.Textarea(attrs={'rows':1, 'cols':30}),
        }

class PresentationForm(forms.ModelForm):
    class Meta:
        model = Presentation
        fields = ('title', 'presenter', 'description', 'file', 'url')
        widgets = {
            'presenter': forms.Textarea(attrs={'rows':1, 'cols':30}),
            'title': forms.Textarea(attrs={'rows':1, 'cols':30}),
            'description': forms.Textarea(attrs={'rows':3, 'cols':30}),
            'url': forms.Textarea(attrs={'rows':1, 'cols':30}),
        }
