from django.shortcuts import render,redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views import View
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login

from django.contrib.auth.forms import UserCreationForm

from .models import Department

# Create your views here.
class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('index')

class RegisterForm(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterForm, self).form_valid(form)

        def get(self, *args, **kwargs):
            if self.request.user.is_authenticated:
                return redirect('index')
            return super(RegisterForm, self).get(*args, **kwargs )


class Home(LoginRequiredMixin, ListView):
    model = Department
    context_object_name = 'departments'
    template_name = 'base/index.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['departments'] = context['departments'].filter(user = self.request.user)

    #     search_input = self.request.GET.get('search-area') or ''
    #     if search_input:
    #         context['departments'] = context['departments'].filter(department__startswith=search_input)
    #     context['search_input'] = search_input
    #     return context
def searchbar(request):
    if request.method == 'GET':
        search = request.GET.get('search-area')
        department = Department.objects.all().filter(department__icontains=search)
        return render(request, 'base/searchbar.html', {'department':department})


class Dept(LoginRequiredMixin, ListView):
    model = Department
    context_object_name = 'departments'


class Policy(LoginRequiredMixin, DetailView):
    model = Department
    context_object_name = 'department'
    template_name = 'base/policy.html'
