from django import forms
from app.models import *
class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'

class WebpageForm(forms.ModelForm):
    class Meta:
        model=Webpage
        #widgets={'name':forms.PasswordInput}
        #exclude={'url'}
        fields='__all__'
        

class AccessForm(forms.ModelForm):
    class Meta:
        model=AccessRecord
        fields='__all__'
