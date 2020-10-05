from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpRequest, request, HttpResponse
from django.views.generic import TemplateView, CreateView, ListView
from .forms import SignUpForm, UserForm, ProfileForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from userprofile.models import Profile
from django.contrib.auth.models import User 
from django.contrib import messages
from connected_kits.models import Kit, Button

# Create your views here.
class HomeView(TemplateView):
    template_name='common/home.html'

class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'common/register.html'
    success_url = reverse_lazy('home')


class DashBoardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'
    model = Button
    context_object_name = "user_kits"
    login_url = reverse_lazy('login')
 
    def get_context_data(self,**kwargs):
        user = self.request.user
        context = super().get_context_data(**kwargs)
        context['buttons'] = Button.objects.filter(user=user)
        return context

class ProfileView(LoginRequiredMixin, TemplateView):
    model = User
    template_name = 'common/profile.html'

class ProfileUpdateView(LoginRequiredMixin, TemplateView):
    user_form = UserForm
    profile_form = ProfileForm
    template_name = 'common/profileUpdate.html'

    def post(self, request):
        post_data = request.POST or None
        file_data = request.FILES or None

        user_form = UserForm(post_data, instance=request.user)
        profile_form = ProfileForm(post_data, file_data, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Your profile was successfully updated....")
            return HttpResponseRedirect(reverse_lazy('profile'))

        context = self.get_context_data(user_form=user_form, profile_form=profile_form)
        
        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)




def change(request, pk):
    button = Button.objects.get(pk=pk)
    status = button.status
    if status == "ON":
        status = "OFF"
    elif status == "OFF":
        status = "ON"
    else:
        print("Something went wrong in button status changing process")
    button.status = status
    button.save()
    return HttpResponseRedirect(reverse_lazy('dashboard'))
