from django import forms


class ContactForm(forms.Form):
        contact_name = forms.CharField(required=False)
        contact_email = forms.EmailField(required=True)
        content = forms.CharField(
            required=True,
            widget=forms.Textarea
        )

        def __init__(self, *args, **kwargs):
            super(ContactForm, self).__init__(*args, **kwargs)
            self.fields['contact_name'].label = "Your name:"
            self.fields['contact_email'].label = "Your email:"
            self.fields['content'].label = "What is the next goal for you/for your business?"