from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import get_template
from .forms import ContactForm

# Create your views here.
def index(request):
    return render(request, 'home/home.html')

def contact(request):
    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
                , '')
            contact_email = request.POST.get(
                'contact_email'
                , '')
            form_content = request.POST.get('content', '')

            template = get_template('email_forms/email_template.txt')

            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content
            }
            content = template.render(context)

            email = EmailMessage(
                "User question",
                content,
                headers= {'Reply-To': contact_email}
            )
            email.send()
            return redirect('contact')

    return render(request, 'email_forms/contact.html', {
        'form': form_class,
    })