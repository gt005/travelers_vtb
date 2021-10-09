from django.views.generic import ListView, TemplateView, View, DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect

from .models import DataUnit, BaseUser


class MainView(ListView):
    template_name = 'index.html'
    model = DataUnit
    context_object_name = 'data_units'


class LoginView(TemplateView):
    template_name = 'login.html'

    def post(self, request):
        exists_users = User.objects.filter(
            username=request.POST.get('username')
        )
        if not exists_users:
            return JsonResponse({
                'message': "User doesn't exist"
            }, status=400)

        user = authenticate(
            username=request.POST.get('username'),
            password=request.POST.get('password')
        )

        if user is not None:
            login(request, user)
        else:
            return JsonResponse({
                'message': "Wrong password"
            }, status=400)

        return redirect('main_page')


class LogoutUserView(View):
    def get(self, request):
        logout(request)
        return redirect('main_page')


class RegistrationView(TemplateView):
    template_name = 'registration.html'

    def post(self, request, **kwargs):
        if request.POST.get('password1') != request.POST.get('password2'):
            return JsonResponse({
                'message': "Пароли не совпадают"
            }, status=401)
        elif not request.POST.get('password1'):
            return JsonResponse({
                'message': "Пароли не совпадают"
            }, status=401)

        user = User(
            username=request.POST.get('username'),
            email=request.POST.get('email'),
            first_name=request.POST.get('name'),
            last_name=request.POST.get("surname"),
        )
        user.set_password(request.POST.get('password2'))
        user.save()

        new_user = BaseUser(  # Написанный класс-расширение для пользователя
            user=user,
        )

        new_user.save()

        if user is not None:
            login(request, user)

        return redirect('main_page')


class ProfileView(TemplateView):
    template_name = 'profile.html'


class CreateDataUnitView(CreateView, LoginRequiredMixin):
    model = DataUnit
    template_name = 'data_unit_create_view.html'
    context_object_name = 'data_unit'
    fields = []




