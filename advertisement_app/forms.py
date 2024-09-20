from django import forms
from .models import Advertisement


class AdvertisementForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AdvertisementForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"
            self.fields['new'].widget = forms.CheckboxInput()
            self.fields['date_and_time'].widget = forms.DateTimeField()
            self.fields['date_and_time'].widget = forms.DateTimeInput(attrs={
                "class": "form-control",
                "type": "datetime-local"  # HTML5 input type for date and time
            })
    class Meta:
        model = Advertisement
        fields = '__all__'

