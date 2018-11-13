from django.shortcuts import render
from .models import Member
from django.views import generic

list_number =  [str(num) for num in range(0,11,1)]

# Create your views here.
class IndexView(generic.ListView):
    model = Member
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        for num in list_number:
            context["qs" + num + "s"] = Member.objects.filter(position=num)
        return context
