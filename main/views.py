from django.views.generic import ListView, TemplateView, View, DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import JsonResponse, Http404
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.core.exceptions import ObjectDoesNotExist

from .models import DataUnit, BaseUser, Category

from random import shuffle


class MainView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)

        context['category_sample'] = list(Category.objects.all())
        shuffle(context['category_sample'])
        context['category_sample'] = context['category_sample'][:5]
        return context


class OffersListView(ListView):
    template_name = 'offers_list.html'
    model = DataUnit

    def get_context_data(self, **kwargs):
        context = super(OffersListView, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        context['offers_list'] = DataUnit.objects.all()
        if self.request.GET.get('category'):
            context['selected_category'] = self.request.GET.get('category')
            context['offers_list'] = filter(
                lambda offer: offer.category.category_title == context['selected_category'],
                context['offers_list'],

            )
        return context


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


class ProfileView(DetailView, LoginRequiredMixin):
    template_name = 'profile.html'
    model = BaseUser
    context_object_name = 'user_profile_obj'
    login_url = '/login/'

    def get_object(self, *args, **kwargs):
        try:
            return self.model.objects.get(
                id=int(self.kwargs['user_id'])
            )
        except (ValueError, ObjectDoesNotExist):
            raise Http404('Такого пользователя не существует')


class CreateDataUnitView(CreateView, LoginRequiredMixin):
    model = DataUnit
    template_name = 'data_unit_create_view.html'
    context_object_name = 'data_unit'
    login_url = '/login/'
    fields = ['title', 'title_image', 'tag']


class OfferView(LoginRequiredMixin, DetailView):
    model = DataUnit
    login_url = '/login/'
    template_name = 'offer_view.html'
    context_object_name = 'offer'

    def get_object(self, *args, **kwargs):
        try:
            return self.model.objects.get(
                id=int(self.kwargs['offer_id'])
            )
        except (ValueError, ObjectDoesNotExist):
            raise Http404('Такого объявления не существует')

