from django.shortcuts import render
from django.urls import reverse_lazy
from datetime import datetime
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserCreationForm,Passwordform,ContactForm
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate,login
from django.views import generic
from .models import Passwords
from django.http import Http404,JsonResponse
from password_generator import PasswordGenerator
from django.views import View
# Create your views here.
def homepage(request):
    if request.method =='GET':
     year = datetime.now().year
     pswrd=''
    #  return render(request,'home.html',{'year':year})
    if request.method == 'POST':
        lowercase = request.POST['lowercase']
        uppercase = request.POST['uppercase']
        symbols = request.POST['symbols']
        numbers = request.POST['numbers']
        pwo = PasswordGenerator()
        pwo.maxlen = int(uppercase) + int(lowercase) +int(numbers)+int(symbols)
        pwo.minuchars = int(uppercase)
        pwo.minlchars = int(lowercase)
        pwo.minnumbers =int(numbers)
        pwo.minschars =int(symbols)
        pswrd = pwo.generate()
        
        year = datetime.now().year
        return JsonResponse(pswrd,safe=False)
        
        
    return render(request,'home.html',{'year':year,'pswrd':pswrd})
       
class Signup(generic.CreateView):
    form_class= UserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'registration/signup.html'
    def form_valid(self, form):
        view = super(Signup,self).form_valid(form)
        username,password = form.cleaned_data.get('username'),form.cleaned_data.get('password1')
        user = authenticate(username=username,password=password)
        login(self.request,user)
        return view

class Add_Secret(LoginRequiredMixin, FormView):
    template_name = 'add_secret.html'
    form_class = Passwordform
    success_url = reverse_lazy('home')
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        success_url = reverse_lazy('home')
        return HttpResponseRedirect(success_url)
@login_required
def ViewSecrets(request,id):
        secrets = Passwords.objects.filter(user=request.user)
        year = datetime.now().year
        return render(request,'my_secrets.html',{'secrets':secrets,'year':year})

def tc(request):
    year = datetime.now().year
    return render(request,'tc.html',{'year':year})

def pp(request):
    year = datetime.now().year
    return render(request,'pp.html',{'year':year})

def about(request):
    year = datetime.now().year
    return render(request,'about.html',{'year':year})
class Contact(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')
    def get_context_data(self, **kwargs):
        context = super(Contact, self).get_context_data(**kwargs)
        context['year'] = datetime.now().year
        return context
        
    def form_valid(self,form):
        form.save()
        year = datetime.now().year
        return render(self.request,'contact.html',{'year':year})
@login_required
def confirmdelete(request,id):
    if request.method=='GET':
     secret = Passwords.objects.get(id=int(id))
     return render(request,'confirm_delete.html',{'secret':secret})
    if request.method=='POST':
        secret =Passwords.objects.get(id=int(id))
        secret.delete()
        url=reverse_lazy('viewsecrets',kwargs={'id':int(id)})
        return HttpResponseRedirect(url)

class UpdateSecret(LoginRequiredMixin, generic.UpdateView):
    model = Passwords
    template_name = 'update_secret.html'
    fields = ['website','password']
    success_url = reverse_lazy('home')

    def get_object(self):
        secret = super(UpdateSecret, self).get_object()
        if not secret.user == self.request.user:
            raise Http404
        return secret


def payment(request):
    return render(request,'payment.html')