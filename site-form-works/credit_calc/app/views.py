from django.shortcuts import render
from django.views.generic import TemplateView

from .forms import CalcForm


class CalcView(TemplateView):
    template_name = "app/calc.html"

    def get(self, request, *args, **kwargs):
        form = CalcForm(self.request.GET)
        if form.is_valid():
            initial_fee = int(self.request.GET.get('initial_fee'))
            rate = int(self.request.GET.get('rate'))
            months_count = int(self.request.GET.get('months_count'))
            common_result = round((initial_fee + initial_fee * rate) / months_count)
            result = round(common_result / months_count, 2)
            return render(request, self.template_name, {'form': form, 'common_result':common_result, 'result': result})
        else:
            return render(request, self.template_name, {'form': form})
