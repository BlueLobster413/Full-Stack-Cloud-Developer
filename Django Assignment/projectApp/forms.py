from django import forms
from . import models

# class GeeksForm(forms.Form):
#     First_name = forms.CharField(max_length=200)
#     Last_name = forms.CharField(max_length=200)
#     Middle_name = forms.CharField(max_length=200)

#     Student_number = forms.IntegerField(help_text='Enter your 9 digit student number')
#     password = forms.CharField(widget= forms.PasswordInput())

#9
# class GeeksForm(forms.Form):
#     title = forms.CharField(widget = forms.Textarea)
#     description = forms.CharField(widget = forms.CheckboxInput)
#     views = forms.IntegerField(widget = forms.TextInput)
#     available = forms.BooleanField(widget = forms.Textarea)

#11
# class GeeksForm(forms.Form):
#     title = forms.CharField(max_length=30)
#     description = forms.CharField(max_length=100)

#13
class GeeksForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = models.GeeksModel11
        # specify fields to be used
        fields = ["title", "description"]