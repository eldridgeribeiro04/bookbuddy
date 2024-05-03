from django.shortcuts import render, redirect
from .models import CustomUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import get_object_or_404
from django.contrib import messages

# Create your views here.

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView

from .forms import CustomUserCreationForm, CustomUserChangeForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"


def profile(request):
    return render(request, "accounts/profile.html")

@login_required
def profile_update_view(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            old_password = form.cleaned_data.get('old_password')
            if user.check_password(old_password):
                new_password = form.cleaned_data.get('password')
                if new_password:
                    user.set_password(new_password)
                    update_session_auth_hash(request, user)
                    user.save()
                    messages.success(request, "Your profile has been updated successfully.")
                    print(messages)
                    return redirect('accounts:update')
            else:
                messages.error(request, "Incorrect password. Please try again")
                print(messages)
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'accounts/profile_update.html', {'form':form })

