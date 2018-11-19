from django.shortcuts import render
from .models import Member
from django.views import generic
from django.utils import timezone

list_number =  [str(num) for num in range(0,11,1)]
year = str(timezone.now()).split("-")[0]

# Create your views here.
class IndexView(generic.ListView):
    model = Member

    def current_year(year,month):
        if month == month in list_year:
            year = str(int(year) - 1)
            return year

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        for num in list_number:
            context["qs" + num + "s"] = Member.objects.filter(position=num,current_year=year)
        return context
