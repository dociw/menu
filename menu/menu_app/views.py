from django.shortcuts import render
from django.views import View


class MenuView(View):

    def get(self, *args, **kwargs):
        return render(self.request, template_name='index.html', context=kwargs)
