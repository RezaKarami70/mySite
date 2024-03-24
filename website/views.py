from django.shortcuts import render
from website.forms import ContactForm, newsletterForm
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib import messages



# Create your views here.
def index_view(request):
    return render(request, 'website/index.html')

def about_view(request):
    return render(request, 'website/about.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            name = form.cleaned_data['name']
            new_form.name = 'unknown'
            new_form.save()
            messages.add_message(request,messages.SUCCESS,'your ticked submited successfully')
        else:
            messages.add_message(request,messages.WARNING,'your ticked did not submited successfully')
    form = ContactForm
    return render(request, 'website/contact.html', {'form': form})

def newsletter_view(request):
    if request.method == 'POST':
        form = newsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')
        