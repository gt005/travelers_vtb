from django.views.generic.base import TemplateView, View


class MainView(TemplateView):
    template_name = 'index.html'
