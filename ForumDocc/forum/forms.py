from django.forms import ModelForm
from .models import Thread, Reply

class ThreadForm(ModelForm):
    class Meta:
        model=Thread
        fields=('title', 'description', 'file')

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['title'].widget.attrs.update({ 'placeholder':'Enter thread'})
    #     self.fields['description'].widget.attrs.update({ 'placeholder':'Enter description'})

class ReplyForm(ModelForm):
    class Meta:
        model=Reply
        fields=('message',)

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['message'].widget.attrs.update({'class':'form-control', 'placeholder':'Post reply'})
