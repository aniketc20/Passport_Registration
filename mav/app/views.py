from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import RegistrationForm, AccountAuthenticationForm


# Create your views here.

def registration_view(request):
    context = {}
    form = RegistrationForm(request.POST or None, request.FILES or None)  # extracts all info from submitted form
    if form.is_valid():  # verifies whether form is valid
        obj = form.save(commit=False)
        obj.save()  # saves form to database
        return render(request, "dashboard.html", context)

    context['registration_form'] = form
    return render(request, 'registration.html', context)


# checks whether request is a GET METHOD or POST METHOD and renders a template
def login_view(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return render(request, "dashboard.html", context)
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            phone_number = request.POST['phone_number']
            password = request.POST['password']
            user = authenticate(phone_number=phone_number, password=password)
            if user:
                login(request, user)
                return redirect("home")  # redirects to home page
    else:
        form = AccountAuthenticationForm()
        context['login_form'] = form

    return render(request, "login.html", context)


# logout view
def logout_view(request):
    request.session.flush()  # deletes session data
    logout(request)
    return redirect('/')


def dashboard(request):
    context = {}
    user = request.user
    if user:
        return render(request, "dashboard.html", context)
