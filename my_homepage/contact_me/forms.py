from django import forms

from my_homepage.contact_me.models import NewContact


class NewContactForm(forms.ModelForm):
    '''Form to process new contacts from the homepage'''

    def __init__(self, *args, **kwargs):
        super(NewContactForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 5}))

    class Meta:
        model = NewContact
        fields = ['name', 'email', 'subject', 'content',]