from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from menu_app.views import MenuView

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('menu/<slug:menu_slug>/<slug:menuitem_slug>/', MenuView.as_view(), name='menu-view')
]
