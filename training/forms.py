from django import forms
from .models import Training

class TrainingModelForm(forms.ModelForm):
    class Meta:
        model = Training
        fields = '__all__'
        exclude = ['trash']
        widgets = {
            'start_date': forms.DateInput(
                attrs={
                    'type': 'date', 'class': 'form-control'}
            )
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'